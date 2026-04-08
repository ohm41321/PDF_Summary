"""
PDF Summarization and Q&A Application - Optimized + Persistent
Backend: FastAPI (async)
LLM: LM Studio (OpenAI-compatible API)
Vector Store: FAISS (with disk cache)
Storage: SQLite + pickle for persistence
OCR: pytesseract for scanned PDFs
"""

import os
import sys
import uuid
import json
import logging
import hashlib
import pickle
import sqlite3
from typing import List, Dict, Any, Optional
from pathlib import Path
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

import fitz  # PyMuPDF
import numpy as np
import faiss
import requests
import tiktoken
import easyocr
from PIL import Image
from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

# PyInstaller resource path helper
def get_resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Configuration
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
CACHE_DIR = Path("cache")
CACHE_DIR.mkdir(exist_ok=True)

LM_STUDIO_URL = os.getenv("LM_STUDIO_URL", "http://localhost:1234")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "bge-m3")
LLM_MODEL = os.getenv("LLM_MODEL", "qwen2.5-7b-instruct")

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
TOP_K = 5
BATCH_SIZE = 10

# Initialize FastAPI
app = FastAPI(title="PDF Summarizer & Q&A API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage
documents: Dict[str, Dict[str, Any]] = {}
index_store: Dict[str, faiss.IndexFlatIP] = {}
chunk_store: Dict[str, List[Dict[str, Any]]] = {}

# Thread pool
executor = ThreadPoolExecutor(max_workers=4)
ocr_reader = None

# ========== Database (SQLite) ==========

def get_db():
    db_path = DATA_DIR / "documents.db"
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id TEXT PRIMARY KEY,
            name TEXT,
            text TEXT,
            short_summary TEXT,
            detailed_summary TEXT,
            num_pages INTEGER,
            num_chunks INTEGER,
            text_length INTEGER,
            uploaded_at TEXT
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_id TEXT,
            role TEXT,
            content TEXT,
            created_at TEXT,
            FOREIGN KEY (document_id) REFERENCES documents(id)
        )
    """)
    conn.commit()
    conn.close()
    logger.info("Database initialized")

def save_document_to_db(doc_id, data):
    conn = get_db()
    conn.execute("""
        INSERT OR REPLACE INTO documents (id, name, text, short_summary, detailed_summary, num_pages, num_chunks, text_length, uploaded_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (doc_id, data['name'], data.get('text', ''), data.get('short_summary', ''), data.get('detailed_summary', ''),
          data.get('num_pages', 0), data.get('num_chunks', 0), data.get('text_length', 0), data.get('uploaded_at', '')))
    conn.commit()
    conn.close()

def load_all_documents():
    conn = get_db()
    rows = conn.execute("SELECT * FROM documents ORDER BY uploaded_at DESC").fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_document_from_db(doc_id):
    conn = get_db()
    row = conn.execute("SELECT * FROM documents WHERE id = ?", (doc_id,)).fetchone()
    conn.close()
    return dict(row) if row else None

def save_chat_to_db(doc_id, role, content):
    conn = get_db()
    conn.execute("""
        INSERT INTO chat_history (document_id, role, content, created_at)
        VALUES (?, ?, ?, ?)
    """, (doc_id, role, content, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def load_chat_from_db(doc_id):
    conn = get_db()
    rows = conn.execute("SELECT role, content FROM chat_history WHERE document_id = ? ORDER BY created_at", (doc_id,)).fetchall()
    conn.close()
    return [dict(row) for row in rows]

# ========== File-based storage for FAISS indexes ==========

def save_index_to_disk(doc_id, index, chunks):
    """Save FAISS index + chunks to disk"""
    index_file = DATA_DIR / f"{doc_id}.faiss"
    chunks_file = DATA_DIR / f"{doc_id}_chunks.pkl"

    faiss.write_index(index, str(index_file))
    with open(chunks_file, 'wb') as f:
        pickle.dump(chunks, f)
    logger.info(f"Saved index + chunks to disk: {doc_id}")

def load_index_from_disk(doc_id):
    """Load FAISS index + chunks from disk"""
    index_file = DATA_DIR / f"{doc_id}.faiss"
    chunks_file = DATA_DIR / f"{doc_id}_chunks.pkl"

    if not index_file.exists() or not chunks_file.exists():
        return None, None

    index = faiss.read_index(str(index_file))
    with open(chunks_file, 'rb') as f:
        chunks = pickle.load(f)
    logger.info(f"Loaded index + chunks from disk: {doc_id}")
    return index, chunks

# ========== Helper Functions ==========

def get_tokenizer():
    try:
        return tiktoken.get_encoding("cl100k_base")
    except Exception:
        return None

def count_tokens(text):
    tokenizer = get_tokenizer()
    if tokenizer:
        return len(tokenizer.encode(text))
    return len(text) // 4

def get_ocr_reader():
    global ocr_reader
    if ocr_reader is None:
        logger.info("Initializing EasyOCR...")
        ocr_reader = easyocr.Reader(['th', 'en'], gpu=False)
    return ocr_reader

def extract_text_with_ocr(image_data, page_num):
    try:
        image = Image.open(BytesIO(image_data))
        reader = get_ocr_reader()
        results = reader.readtext(np.array(image))
        return '\n'.join([r[1] for r in results])
    except Exception as e:
        logger.error(f"OCR failed page {page_num}: {e}")
        return ""

def extract_text_from_pdf(file_path):
    text_parts = []
    doc = fitz.open(file_path)
    total_pages = len(doc)
    logger.info(f"Processing {total_pages} pages")

    for page_num, page in enumerate(doc):
        text = page.get_text()
        if text.strip():
            text_parts.append(f"[Page {page_num + 1}]\n{text}")
        else:
            logger.info(f"Page {page_num + 1} needs OCR...")
            try:
                pix = page.get_pixmap(dpi=300)
                ocr_text = extract_text_with_ocr(pix.tobytes("png"), page_num + 1)
                if ocr_text.strip():
                    text_parts.append(f"[Page {page_num + 1} (OCR)]\n{ocr_text}")
            except Exception as e:
                logger.error(f"OCR failed page {page_num + 1}: {e}")
    doc.close()
    return "\n\n".join(text_parts) if text_parts else extract_text_with_ocr_full(file_path)

def extract_text_with_ocr_full(file_path):
    text_parts = []
    doc = fitz.open(file_path)
    for page_num, page in enumerate(doc):
        try:
            pix = page.get_pixmap(dpi=300)
            ocr_text = extract_text_with_ocr(pix.tobytes("png"), page_num + 1)
            if ocr_text.strip():
                text_parts.append(f"[Page {page_num + 1}]\n{ocr_text}")
        except Exception as e:
            logger.error(f"OCR failed page {page_num + 1}: {e}")
    doc.close()
    return "\n\n".join(text_parts)

def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    tokenizer = get_tokenizer()
    chunks = []
    if tokenizer:
        tokens = tokenizer.encode(text)
        start = 0
        while start < len(tokens):
            end = start + chunk_size
            chunk_text = tokenizer.decode(tokens[start:end])
            page_match = chunk_text.split("\n")[0] if "[Page" in chunk_text else ""
            chunks.append({"text": chunk_text.strip(), "page_reference": page_match, "start_token": start, "end_token": end})
            start += (chunk_size - overlap)
    else:
        chars_per_token = 4
        chunk_chars = chunk_size * chars_per_token
        overlap_chars = overlap * chars_per_token
        start = 0
        while start < len(text):
            end = start + chunk_chars
            chunk_text = text[start:end]
            page_match = chunk_text.split("\n")[0] if "[Page" in chunk_text else ""
            chunks.append({"text": chunk_text.strip(), "page_reference": page_match, "start_char": start, "end_char": end})
            start += (chunk_chars - overlap_chars)
    logger.info(f"Created {len(chunks)} chunks")
    return chunks

def get_cache_key(text):
    return hashlib.md5(text.encode()).hexdigest()

def load_embeddings_from_cache(doc_id):
    cache_file = CACHE_DIR / f"{doc_id}_embeddings.pkl"
    if cache_file.exists():
        with open(cache_file, 'rb') as f:
            return pickle.load(f)
    return None

def save_embeddings_to_cache(doc_id, embeddings):
    cache_file = CACHE_DIR / f"{doc_id}_embeddings.pkl"
    with open(cache_file, 'wb') as f:
        pickle.dump(embeddings, f)

def get_embeddings_batch(texts):
    endpoint = f"{LM_STUDIO_URL}/v1/embeddings"
    all_embeddings = []

    for i in range(0, len(texts), BATCH_SIZE):
        batch = texts[i:i + BATCH_SIZE]
        try:
            if len(batch) == 1:
                response = requests.post(endpoint, json={"model": EMBEDDING_MODEL, "input": batch[0]}, timeout=30)
                if response.status_code == 200:
                    data = response.json()
                    all_embeddings.append(data["data"][0]["embedding"])
                    continue

            response = requests.post(endpoint, json={"model": EMBEDDING_MODEL, "input": batch}, timeout=60)
            if response.status_code == 200:
                data = response.json()
                for item in data.get("data", []):
                    all_embeddings.append(item["embedding"])
                continue
        except Exception as e:
            logger.warning(f"Batch embedding failed: {e}")

        for text in batch:
            try:
                response = requests.post(endpoint, json={"model": EMBEDDING_MODEL, "input": text}, timeout=30)
                if response.status_code == 200:
                    all_embeddings.append(response.json()["data"][0]["embedding"])
                else:
                    all_embeddings.append(np.random.rand(384).astype(np.float32))
            except:
                all_embeddings.append(np.random.rand(384).astype(np.float32))

    return np.array(all_embeddings)

def get_embeddings(texts):
    if len(texts) == 1:
        cache_key = get_cache_key(texts[0])
        cached = load_embeddings_from_cache(cache_key)
        if cached is not None:
            return cached
    embeddings = get_embeddings_batch(texts)
    if len(texts) == 1:
        save_embeddings_to_cache(get_cache_key(texts[0]), embeddings)
    return embeddings

def call_llm(prompt, system_message=None):
    messages = []
    if system_message:
        messages.append({"role": "system", "content": system_message})
    messages.append({"role": "user", "content": prompt})
    try:
        response = requests.post(
            f"{LM_STUDIO_URL}/v1/chat/completions",
            json={"model": LLM_MODEL, "messages": messages, "temperature": 0.3, "max_tokens": 2000},
            timeout=120
        )
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        return f"Error: Could not get response (status: {response.status_code})"
    except Exception as e:
        return f"Error: Could not connect to LM Studio - {str(e)}"

def generate_short_summary(text, custom_prompt=None):
    if custom_prompt:
        prompt = custom_prompt + "\n\nDocument:\n" + text[:8000]
    else:
        prompt = f"""Create a SHORT summary of the following document.
Requirements:
- 3-5 bullet points
- Each bullet captures a key point
- Concise
- Focus on most important information

Document:
{text[:8000]}

SHORT SUMMARY (3-5 bullet points):"""
    return call_llm(prompt, "You are a helpful assistant that creates concise summaries.")

def generate_detailed_summary(text, custom_prompt=None):
    if custom_prompt:
        prompt = custom_prompt + "\n\nDocument:\n" + text[:10000]
    else:
        prompt = f"""Create a DETAILED summary of the following document.
Requirements:
- Well-structured summary with sections
- Cover main topics, key findings, important details
- Use headings for organization
- Comprehensive but organized

Document:
{text[:10000]}

DETAILED SUMMARY:"""
    return call_llm(prompt, "You are a helpful assistant that creates detailed, well-structured summaries.")

def retrieve_relevant_chunks(document_id, query, top_k=TOP_K):
    if document_id not in index_store or document_id not in chunk_store:
        return []
    try:
        query_embedding = get_embeddings([query])
        query_embedding = query_embedding / np.linalg.norm(query_embedding, axis=1, keepdims=True)
        index = index_store[document_id]
        chunks = chunk_store[document_id]
        distances, indices = index.search(query_embedding.astype(np.float32), min(top_k, len(chunks)))
        results = []
        for i, idx in enumerate(indices[0]):
            if idx < len(chunks):
                chunk = chunks[idx].copy()
                chunk["score"] = float(distances[0][i])
                results.append(chunk)
        return results
    except Exception as e:
        logger.error(f"Retrieval error: {e}")
        return []

def generate_answer(question, context_chunks):
    if not context_chunks:
        return "I don't have enough context to answer this question."
    context = "\n\n".join([f"[Context {i+1}]\n{chunk['text']}" for i, chunk in enumerate(context_chunks)])
    prompt = f"""Answer ONLY based on the provided context.
Instructions:
- Answer ONLY based on the context
- If not in context, say "The document doesn't contain information about this"
- Be specific and cite relevant details

Context:
{context}

Question: {question}

Answer:"""
    return call_llm(prompt, "You are a helpful assistant that answers questions based ONLY on the provided context.")

# ========== Process single document ==========

def process_document(file_path, filename, document_id=None):
    if document_id is None:
        document_id = str(uuid.uuid4())

    # Extract text
    text = extract_text_from_pdf(str(file_path))
    if not text.strip():
        raise ValueError("Could not extract text from PDF")

    # Chunk
    chunks = chunk_text(text)

    # Embeddings (batch + cache)
    chunk_texts = [chunk["text"] for chunk in chunks]
    embeddings = get_embeddings(chunk_texts)

    # Normalize
    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    norms[norms == 0] = 1
    normalized_embeddings = embeddings / norms

    # Create FAISS index
    dimension = normalized_embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)
    index.add(normalized_embeddings.astype(np.float32))

    num_pages = len(fitz.open(file_path))

    # Store in memory
    doc_data = {"name": filename, "text": text, "chunks": chunks, "uploaded_at": datetime.now().isoformat(),
                "num_pages": num_pages, "num_chunks": len(chunks), "text_length": len(text)}
    documents[document_id] = doc_data
    index_store[document_id] = index
    chunk_store[document_id] = chunks

    # Save to disk (persistent)
    save_document_to_db(document_id, doc_data)
    save_index_to_disk(document_id, index, chunks)

    return {
        "success": True, "document_id": document_id, "filename": filename,
        "num_pages": num_pages, "num_chunks": len(chunks), "text_length": len(text)
    }

def load_documents_from_disk():
    """Load all previously processed documents from disk"""
    docs = load_all_documents()
    count = 0

    for doc_row in docs:
        doc_id = doc_row['id']

        # Try loading index from disk
        index, chunks = load_index_from_disk(doc_id)
        if index is not None and chunks is not None:
            # Load full text from DB
            full_doc = get_document_from_db(doc_id)
            if full_doc:
                documents[doc_id] = {
                    "name": full_doc['name'],
                    "text": full_doc.get('text', ''),
                    "chunks": chunks,
                    "uploaded_at": full_doc.get('uploaded_at', ''),
                    "num_pages": full_doc.get('num_pages', 0),
                    "num_chunks": full_doc.get('num_chunks', 0),
                    "text_length": full_doc.get('text_length', 0),
                    "short_summary": full_doc.get('short_summary', ''),
                    "detailed_summary": full_doc.get('detailed_summary', '')
                }
                index_store[doc_id] = index
                chunk_store[doc_id] = chunks
                count += 1
                logger.info(f"Loaded from disk: {full_doc['name']}")
        else:
            logger.warning(f"Index files missing for: {doc_row['name']}")

    logger.info(f"Loaded {count} documents from disk")
    return count

# ========== API Endpoints ==========

class AskRequest(BaseModel):
    document_id: str
    question: str

class AskResponse(BaseModel):
    answer: str
    source_chunks: List[Dict[str, Any]]

@app.on_event("startup")
async def startup():
    init_db()
    load_documents_from_disk()

@app.get("/")
async def root():
    html_path = get_resource_path("index.html")
    logger.info(f"Looking for index.html at: {html_path}")
    logger.info(f"File exists: {os.path.exists(html_path)}")
    logger.info(f"MEIPASS: {getattr(sys, '_MEIPASS', 'Not set')}")
    return FileResponse(html_path)

@app.get("/documents")
async def list_documents():
    return {
        "documents": [
            {"id": doc_id, "name": doc["name"], "num_chunks": len(doc.get("chunks", [])),
             "uploaded_at": doc.get("uploaded_at", ""), "num_pages": doc.get("num_pages", 0)}
            for doc_id, doc in documents.items()
        ]
    }

@app.delete("/documents/{document_id}")
async def delete_document(document_id: str):
    """Delete a document and all associated data"""
    if document_id not in documents:
        raise HTTPException(status_code=404, detail="Document not found")

    try:
        # Remove from memory
        documents.pop(document_id, None)
        index_store.pop(document_id, None)
        chunk_store.pop(document_id, None)

        # Remove from DB
        conn = get_db()
        conn.execute("DELETE FROM documents WHERE id = ?", (document_id,))
        conn.execute("DELETE FROM chat_history WHERE document_id = ?", (document_id,))
        conn.commit()
        conn.close()

        # Remove files from disk
        index_file = DATA_DIR / f"{document_id}.faiss"
        chunks_file = DATA_DIR / f"{document_id}_chunks.pkl"
        pdf_file = UPLOAD_DIR / f"{document_id}.pdf"

        for f in [index_file, chunks_file, pdf_file]:
            if f.exists():
                f.unlink()
                logger.info(f"Deleted file: {f}")

        logger.info(f"Document deleted: {document_id}")
        return {"success": True, "message": "Document deleted"}
    except Exception as e:
        logger.error(f"Delete error: {e}")
        raise HTTPException(status_code=500, detail=f"Error deleting document: {str(e)}")

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files accepted")

    document_id = str(uuid.uuid4())
    file_path = UPLOAD_DIR / f"{document_id}.pdf"

    try:
        content = await file.read()
        with open(file_path, "wb") as f:
            f.write(content)

        return process_document(file_path, file.filename, document_id)
    except Exception as e:
        logger.error(f"Upload error: {e}")
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {str(e)}")

@app.post("/upload/multiple")
async def upload_multiple(files: List[UploadFile] = File(...)):
    """Upload multiple PDFs at once"""
    results = []
    for file in files:
        if not file.filename.lower().endswith('.pdf'):
            results.append({"filename": file.filename, "success": False, "error": "Not a PDF"})
            continue

        document_id = str(uuid.uuid4())
        file_path = UPLOAD_DIR / f"{document_id}.pdf"

        try:
            content = await file.read()
            with open(file_path, "wb") as f:
                f.write(content)

            result = process_document(file_path, file.filename, document_id)
            results.append(result)
        except Exception as e:
            results.append({"filename": file.filename, "success": False, "error": str(e)})

    return {"results": results, "total": len(results), "success_count": sum(1 for r in results if r.get("success"))}

@app.post("/summarize")
async def summarize(document_id: str = Form(...), short_prompt: str = Form(None), detailed_prompt: str = Form(None)):
    if document_id not in documents:
        raise HTTPException(status_code=404, detail="Document not found")

    text = documents[document_id]["text"]
    short_summary = generate_short_summary(text, short_prompt)
    detailed_summary = generate_detailed_summary(text, detailed_prompt)

    documents[document_id]["short_summary"] = short_summary
    documents[document_id]["detailed_summary"] = detailed_summary

    # Update DB
    conn = get_db()
    conn.execute("UPDATE documents SET short_summary = ?, detailed_summary = ? WHERE id = ?",
                 (short_summary, detailed_summary, document_id))
    conn.commit()
    conn.close()

    return {"success": True, "document_id": document_id, "short_summary": short_summary, "detailed_summary": detailed_summary}

@app.post("/ask", response_model=AskResponse)
async def ask_question(request: AskRequest):
    if request.document_id not in documents:
        raise HTTPException(status_code=404, detail="Document not found")

    relevant_chunks = retrieve_relevant_chunks(request.document_id, request.question)
    if not relevant_chunks:
        return AskResponse(answer="I couldn't find relevant information in the document.", source_chunks=[])

    answer = generate_answer(request.question, relevant_chunks)
    source_chunks = [{"text": chunk["text"][:500] + "...", "page_reference": chunk.get("page_reference", ""), "score": chunk.get("score", 0)} for chunk in relevant_chunks[:3]]

    # Save chat to DB
    save_chat_to_db(request.document_id, "user", request.question)
    save_chat_to_db(request.document_id, "ai", answer)

    return AskResponse(answer=answer, source_chunks=source_chunks)

@app.get("/chat/{document_id}")
async def get_chat_history(document_id: str):
    history = load_chat_from_db(document_id)
    return {"chat": history}

@app.get("/health")
async def health_check():
    try:
        response = requests.get(f"{LM_STUDIO_URL}/v1/models", timeout=5)
        if response.status_code == 200:
            models_data = response.json()
            available_models = [m.get("id", "unknown") for m in models_data.get("data", [])]
            lm_status = f"connected ({len(available_models)} models)"
        else:
            lm_status = f"error ({response.status_code})"
            available_models = []
    except:
        lm_status = "not reachable"
        available_models = []

    return {"status": "healthy", "lm_studio_status": lm_status, "available_models": available_models,
            "embedding_model": EMBEDDING_MODEL, "llm_model": LLM_MODEL,
            "loaded_documents": len(documents)}

@app.get("/models")
async def list_models():
    try:
        response = requests.get(f"{LM_STUDIO_URL}/v1/models", timeout=5)
        if response.status_code == 200:
            models_data = response.json()
            models = []
            for m in models_data.get("data", []):
                mid = m.get("id", "unknown")
                mname = m.get("name", mid)
                lower = mid.lower() + mname.lower()
                mtype = "embedding" if any(kw in lower for kw in ["embed", "bge", "e5", "minilm", "sentence"]) else "chat"
                models.append({"id": mid, "name": mname, "type": mtype})
            return {"success": True, "models": models, "current_llm": LLM_MODEL, "current_embedding": EMBEDDING_MODEL}
        return {"success": False, "error": f"Status: {response.status_code}"}
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.post("/models/switch")
async def switch_model(request: Request):
    global LLM_MODEL, EMBEDDING_MODEL
    try:
        data = await request.json()
        if "llm_model" in data: LLM_MODEL = data["llm_model"]
        if "embedding_model" in data: EMBEDDING_MODEL = data["embedding_model"]
        return {"success": True, "llm_model": LLM_MODEL, "embedding_model": EMBEDDING_MODEL}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/export/{document_id}")
async def export_summary(document_id: str):
    if document_id not in documents:
        raise HTTPException(status_code=404, detail="Document not found")
    doc = documents[document_id]
    text = f"""PDF Summary Export
{'='*50}
Document: {doc['name']}
Exported: {doc.get('uploaded_at', 'Unknown')}

{'='*50}
SHORT SUMMARY
{'='*50}
{doc.get('short_summary', 'Not generated')}

{'='*50}
DETAILED SUMMARY
{'='*50}
{doc.get('detailed_summary', 'Not generated')}

{'='*50}
Document Info
{'='*50}
- Pages: {doc.get('num_pages', 0)}
- Text: {doc.get('text_length', 0)} chars
- Chunks: {doc.get('num_chunks', 0)}
"""
    return JSONResponse({"success": True, "content": text, "filename": f"summary_{doc['name'].replace('.pdf', '')}.txt"})

@app.get("/index.html")
async def get_frontend():
    return FileResponse(get_resource_path("index.html"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
