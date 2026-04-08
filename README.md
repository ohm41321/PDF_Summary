# 📄 PDF Summarizer & Q&A

**AI-Powered PDF Analysis Tool** - Summarize documents and ask questions with AI

> 🚀 **No Python Installation Required** - Just download and run!

---

## 🚀 Quick Start (For Users)

### Download the .exe

1. Go to **[Releases](https://github.com/ohm41321/PDF_Summary/releases)**
2. Download the latest version (e.g., `PDFSummarizer-v1.0.0-Windows.zip`)
3. Extract the ZIP file
4. Double-click **`PDFSummarizer.exe`**
5. Your browser will open to `http://localhost:8000`

### Requirements

- ✅ Windows 10/11 (64-bit)
- ✅ 8GB RAM minimum
- ✅ LM Studio (for AI features)

### First Time Setup

#### Step 1: Install LM Studio

1. Download from: https://lmstudio.ai/
2. Install and open the program
3. Download a model (see recommendations below)
4. Click **"Start Server"**

#### Step 2: Run the App

1. Open the extracted folder
2. Double-click **`PDFSummarizer.exe`**
3. Start uploading PDFs!

---

## 📖 How to Use

### 1️⃣ Upload PDF
- Drag and drop or click to select
- Supports multiple files

### 2️⃣ Generate Summaries
- Click **"Generate"** button
- View short (3-5 bullets) or detailed summary
- Click **Export** to download

### 3️⃣ Ask Questions
- Type your question in the chat box
- Click suggested questions
- AI answers based on PDF content

### 4️⃣ Switch Language
- Click 🇹🇭 / 🌐 button in top-right corner

---

## 🤖 LM Studio Setup

### Recommended Models (Thai Language Support)

| Type | Model | Size | Best For |
|---|---|---|---|
| **LLM** | **Typhoon-v1.5x-7B** 🇹🇭 | ~7B | Thai documents (best quality) |
| **LLM** | **Qwen2.5-7B-Instruct** | ~7B | Thai + English mix |
| **Embedding** | **bge-m3** | ~2GB | 100+ languages |
| **Embedding** | **BAAI/bge-base-th** 🇹🇭 | ~500MB | Thai-specific |

### How to Download Models

1. Open LM Studio
2. Click 🔍 **Search** icon
3. Type model name (e.g., `typhoon-v1.5x-7b`)
4. Click **Download** (recommend Q4_K_M version)
5. Wait for download to complete

### How to Start the Server

1. Go to **🖥️ Local Server** tab
2. Select your downloaded model
3. Click **"Start Server"**
4. Wait for green indicator
5. Run PDFSummarizer.exe!

---

## ❓ Troubleshooting

| Problem | Solution |
|---|---|
| **App won't open** | ✓ Check LM Studio is running<br/>✓ Click "Start Server" in LM Studio |
| **Summary fails/errors** | ✓ Verify model is downloaded<br/>✓ Try different model |
| **Q&A not working** | ✓ Check Server shows green<br/>✓ Try simple questions first |
| **PDF upload stuck** | ✓ File may be too large (>100 pages)<br/>✓ Wait a moment |
| **Windows Defender warning** | ✓ Click "Run anyway" (false positive)<br/>✓ Add exception |

---

## 📸 Screenshots

<img width="2483" height="1355" alt="image" src="https://github.com/user-attachments/assets/00558d88-f28a-498b-b58f-c8ddd415e7ee" />

---

## 📁 File Structure (After Extracting)

```
PDFSummarizer/
├── PDFSummarizer.exe      ← Double-click to run
├── index.html             ← Web interface
├── uploads/               ← PDF storage
├── data/                  ← Database
└── cache/                 ← Cache files
```

---

## 📝 Important Notes

- ⚠️ **Keep LM Studio open** while using the app
- 💾 All data stored locally (no cloud)
- 🔄 Restart app anytime - data persists
- 🌐 Works offline (after initial setup)
- 📄 PDF files only (no Word, Excel)

---

## 🛠️ For Developers

### Running from Source

#### Prerequisites

- Python 3.10+
- pip (Python package manager)

#### Setup

```bash
# Clone the repository
git clone https://github.com/ohm41321/Doc_Summary.git
cd Doc_Summary

# Run setup (installs dependencies)
setup.bat

# Start the application
start.bat
```

#### Manual Setup (Alternative)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Building the .exe

```bash
# Quick build (recommended)
build_debug.bat

# Full build with all features
build_exe.bat
```

### Project Structure (Development)

```
Doc_Summary/
├── main.py                # FastAPI backend
├── app_launcher.py        # PyInstaller entry point
├── index.html             # Frontend interface
├── requirements.txt       # Python dependencies
├── setup.bat             # Auto-setup script
├── start.bat             # Quick start script
├── build_debug.bat       # Build .exe (debug mode)
├── build_exe.bat         # Build .exe (production)
└── [other dev files...]
```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit with clear messages (`git commit -m 'feat: add amazing feature'`)
5. Push to your branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 🤝 Support

If you find this project helpful, please consider giving it a ⭐!

[☕ Buy me a coffee](https://tipme.in.th/athitfkm)

---

## 📜 License

MIT License - See [LICENSE](LICENSE) file for details

---

## 📋 Release Notes

See [RELEASE_NOTES.md](RELEASE_NOTES.md) for version history and upcoming features.

---

**Developed by [ItsAthtz](https://github.com/ohm41321)**
