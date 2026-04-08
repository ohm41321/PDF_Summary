# Release Notes

## Version 1.0.0 (April 2026)

**Initial Release** 🎉

### ✨ Features

- 📤 **PDF Upload**
  - Drag-and-drop support
  - Multiple file upload
  - Progress indicator with steps
  - OCR for scanned PDFs

- 🤖 **AI Summarization**
  - Short summary (3-5 bullet points)
  - Detailed summary with sections
  - Customizable summary prompts
  - Export to text file

- 💬 **Smart Q&A**
  - Context-aware answers
  - Source references
  - Suggested questions
  - Chat history export

- 🇹🇭 **Language Support**
  - Thai language UI
  - English language UI
  - One-click language switch
  - Thai/English document support

- 🚀 **Easy Setup**
  - One-click setup (`setup.bat`)
  - One-click start (`start.bat`)
  - Standalone .exe build option
  - Automatic LM Studio detection

- 💾 **Persistence**
  - Documents saved between sessions
  - FAISS index caching
  - Embedding caching
  - Chat history storage

### 🔧 Technical Details

- **Backend:** FastAPI (Python)
- **Frontend:** HTML + JavaScript + TailwindCSS
- **AI Engine:** LM Studio (OpenAI-compatible API)
- **Vector Search:** FAISS
- **PDF Processing:** PyMuPDF + EasyOCR
- **Embeddings:** BGE-M3 / Multilingual models

### 📦 Build Options

- Run from source (Python)
- Standalone .exe (PyInstaller)
- No Python installation required for .exe version

### ⚙️ Requirements

**For Source Version:**
- Python 3.10+
- 8GB RAM minimum
- LM Studio running

**For .exe Version:**
- Windows 10/11
- 8GB RAM minimum
- LM Studio running

### 🎯 Recommended Models

**LLM Models:**
- Qwen2.5-7B-Instruct (All-rounder)
- Typhoon-v1.5x-7B (Thai specialist)
- Llama-3.1-8B-Instruct (Meta's model)

**Embedding Models:**
- bge-m3 (Best multilingual)
- BAAI/bge-base-th (Thai specialist)

### 🐛 Known Issues

- First run with EasyOCR takes longer (downloads Thai language model)
- Large PDFs (>50 pages) may take 2-3 minutes to process
- Windows Firewall may prompt on first run

### 📝 Notes

- All data stored locally (no cloud storage)
- Documents persist between sessions
- Requires active LM Studio server for AI features
- Works offline after initial setup

---

## Future Roadmap

### Version 1.1.0 (Planned)
- [ ] Batch summary generation
- [ ] PDF annotation support
- [ ] Custom model configuration UI
- [ ] Dark/Light theme toggle

### Version 1.2.0 (Planned)
- [ ] Multiple document comparison
- [ ] Keyword extraction
- [ ] Timeline visualization
- [ ] Export to PDF

### Version 2.0.0 (Planned)
- [ ] Cloud model support (OpenAI, etc.)
- [ ] User authentication
- [ ] Multi-user support
- [ ] Web deployment option

---

**Download Latest:** https://github.com/ohm41321/Doc_Summary/releases

**Report Issues:** https://github.com/ohm41321/Doc_Summary/issues
