# 📄 PDF Summarizer & Q&A

**AI-Powered PDF Analysis** - Upload documents, generate summaries, and ask questions in Thai & English

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-green.svg)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**โปรเเกรมสรุปเอกสารเเละตอบคำถามด้วย AI** - อัปโหลด PDF, สรุปเนื้อหา, ถามตอบเกี่ยวกับเอกสาร รองรับภาษาไทย-อังกฤษ

---

## ✨ Features

| Feature | Description |
|---|---|
| 📤 **PDF Upload** | Drag-and-drop or click to upload, supports multiple files |
| 🤖 **AI Summarization** | Generate short (3-5 bullets) and detailed summaries |
| 💬 **Smart Q&A** | Ask questions about document content with AI-powered answers |
| 🇹🇭 **Thai/English Support** | Switch UI language with one click |
| 📥 **Export Results** | Download summaries and chat history as text files |
| 🔍 **Model Selection** | Choose your preferred LLM and embedding models |
| 💡 **Suggested Questions** | Quick-start with preset questions |
| 💾 **Persistent Storage** | Documents saved between sessions |
| 🚀 **One-Click Start** | Easy setup with `setup.bat` and `start.bat` |

---

## 📸 Screenshots

*Add screenshots of your application here*

---

## 🚀 Quick Start

### Option 1: Run .exe (Recommended for Users)

1. Download the latest release from [Releases](../../releases)
2. Extract the ZIP file
3. Double-click `PDFSummarizer.exe`
4. **No Python installation required!**

### Option 2: Run from Source (For Developers)

```bash
# 1. Clone the repository
git clone https://github.com/ohm41321/Doc_Summary.git
cd Doc_Summary

# 2. Setup (one-click)
setup.bat

# 3. Run
start.bat
```

**Manual Setup:**
```bash
# Create virtual environment
python -m venv venv

# Activate
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

The app will automatically open at **http://localhost:8000**

---

## 🔧 Setup LM Studio

**LM Studio is required for AI features!**

### Step 1: Download LM Studio

📥 Download from: https://lmstudio.ai/

### Step 2: Install & Launch

1. Install LM Studio
2. Open LM Studio
3. Click the **"Search"** tab (magnifying glass icon)

### Step 3: Download Models

#### ⭐ Recommended LLM Models (for Chat & Summarization)

| Model | Size | RAM Required | Thai Support | Download Link |
|---|---|---|---|---|
| **Qwen2.5-7B-Instruct** | ~7B | 8GB | ⭐⭐⭐⭐⭐ | Search: `qwen2.5-7b-instruct` |
| **Typhoon-v1.5x-7B** 🇹🇭 | ~7B | 8GB | ⭐⭐⭐⭐⭐ | Search: `typhoon-v1.5x-7b` |
| **Llama-3.1-8B-Instruct** | ~8B | 10GB | ⭐⭐⭐⭐ | Search: `llama-3.1-8b-instruct` |
| **Mistral-7B-Instruct** | ~7B | 8GB | ⭐⭐⭐ | Search: `mistral-7b-instruct` |

#### 🔤 Recommended Embedding Models (for Document Search)

| Model | Thai Support | Search Term |
|---|---|---|
| **bge-m3** | ⭐⭐⭐⭐⭐ | Search: `bge-m3` |
| **multilingual-e5-large** | ⭐⭐⭐⭐ | Search: `multilingual-e5-large` |
| **BAAI/bge-base-th** 🇹🇭 | ⭐⭐⭐⭐⭐ | Search: `bge-base-th` |

### Step 4: Start Server

1. Go to **"Local Server"** tab (server icon)
2. Select your downloaded model
3. Click **"Start Server"** button
4. The app will automatically detect and connect to it

---

## 🇹🇭 Best Models for Thai Language

### 🏆 Top Picks

| Purpose | Model | Why? |
|---|---|---|
| **Chat/Summary** | **Typhoon-v1.5x-7B** | Developed by SCB 10X, best Thai understanding |
| **Chat/Summary** | **Qwen2.5-7B-Instruct** | Excellent multilingual support |
| **Embedding** | **bge-m3** | Best multilingual embedding (100+ languages) |
| **Embedding** | **BAAI/bge-base-th** | Specifically trained for Thai |

### 📥 How to Download Models

**Method 1: Via LM Studio UI**
1. Open LM Studio
2. Click **Search** icon (🔍)
3. Type model name (e.g., `typhoon-v1.5x-7b`)
4. Click **Download** button
5. Wait for download to complete

**Method 2: Via HuggingFace**
1. Visit https://huggingface.co
2. Search for the model
3. Download the GGUF version
4. Place in LM Studio models folder

### 💡 Pro Tips

- **Typhoon-v1.5x-7B** understands Thai context better than any other model
- **Qwen2.5-7B** is a good all-rounder for Thai + English
- **bge-m3** handles mixed Thai-English documents perfectly
- Use **4-bit quantization** (Q4_K_M) for faster loading with minimal quality loss

---

## 📖 Usage Guide

### 1️⃣ Upload PDF

- Click the upload area or **drag & drop** your PDF
- Supports multiple files at once
- Wait for processing (shows progress steps)

### 2️⃣ Generate Summary

- Click the **"Generate"** button
- View **SHORT SUMMARY** (3-5 bullet points)
- View **DETAILED SUMMARY** (comprehensive breakdown)
- Click **⛶** icon to expand summary to full screen
- Click **Export** to download as text file

### 3️⃣ Ask Questions

- Type your question in the chat box
- Press **Enter** or click **Send**
- Click **suggested questions** (chips) for quick start
- Answers include source references from the document

### 4️⃣ Switch Language

- Click the **🇹🇭 / 🌐** button in the top-right corner
- UI language switches instantly

### 5️⃣ Change Models

- Use the model dropdowns (appears when connected to LM Studio)
- Changes apply immediately

### 6️⃣ Export Results

- Click **Export** to download summary
- Click **Export Chat** to download conversation

---

## ⚙️ Configuration

### Environment Variables (Optional)

Create a `.env` file:

```bash
# LM Studio server URL
LM_STUDIO_URL=http://localhost:1234

# LLM Model
LLM_MODEL=qwen2.5-7b-instruct

# Embedding Model
EMBEDDING_MODEL=bge-m3
```

### Check LM Studio Connection

```bash
python check_lmstudio.py
```

---

## 📁 Project Structure

```
Doc_Summary/
├── main.py              # FastAPI backend
├── app_launcher.py      # PyInstaller entry point
├── index.html           # Frontend UI
├── requirements.txt     # Python dependencies
├── setup.bat           # One-click setup script
├── start.bat           # One-click start script
├── build_debug.bat     # Build to .exe script
├── check_lmstudio.py   # LM Studio detection utility
├── README.md           # This file
├── HOW_TO_BUILD_EXE.md # Guide for building .exe
├── uploads/            # Uploaded PDFs (auto-created)
├── data/               # Database & indexes (auto-created)
└── cache/              # Embedding cache (auto-created)
```

---

## 🔨 Build to .exe

See [HOW_TO_BUILD_EXE.md](HOW_TO_BUILD_EXE.md) for detailed instructions.

**Quick Build:**
```bash
build_debug.bat
```

The executable will be in `dist/PDFSummarizer/`

---

## 🛠️ Troubleshooting

| Problem | Solution |
|---|---|
| **LM Studio not connecting** | ✓ Make sure LM Studio is running<br>✓ Click "Start Server" in LM Studio<br>✓ Check the status indicator (green = connected) |
| **500 Internal Server Error** | ✓ Make sure LM Studio has a model loaded<br>✓ Check that the server is started |
| **Model not showing** | ✓ Verify model is loaded in LM Studio<br>✓ Use exact model name |
| **Upload fails** | ✓ Ensure file is PDF format<br>✓ Check file size (large files take longer) |
| **Empty summary** | ✓ Make sure PDF has extractable text<br>✓ Try a different model<br>✓ Check LM Studio server is running |
| **Build fails** | ✓ Run: `pip install -r requirements.txt`<br>✓ Run: `pip install pyinstaller`<br>✓ Close any running instances |

---

## 📋 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main application |
| `/upload` | POST | Upload PDF file |
| `/upload/multiple` | POST | Upload multiple PDFs |
| `/summarize` | POST | Generate summaries |
| `/ask` | POST | Ask a question |
| `/documents` | GET | List uploaded documents |
| `/models` | GET | List available LM Studio models |
| `/models/switch` | POST | Switch active models |
| `/export/{id}` | GET | Export summaries |
| `/chat/{id}` | GET | Get chat history |
| `/health` | GET | Health check & LM status |

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ☕ Support

If you find this project helpful, consider buying me a coffee!

[![TipMe](https://img.shields.io/badge/TipMe-Support-yellow?style=for-the-badge&logo=coffee)](https://tipme.in.th/athitfkm)

---

## 🌟 Star History

If this project helped you, please give it a ⭐ star!

---

**Made with ❤️ by [ItsAthitz](https://github.com/ohm41321)**
