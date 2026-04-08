# 📁 Repository Structure

This repository is organized for **users first**, with developer resources below.

---

## For Users: Download & Use

### Get the Application

1. Go to **[Releases](https://github.com/ohm41321/Doc_Summary/releases)**
2. Download the latest ZIP (e.g., `PDFSummarizer-v1.0.0-Windows.zip`)
3. Extract and run **`PDFSummarizer.exe`**

### What You Get

After extracting the ZIP:

```
PDFSummarizer/
├── PDFSummarizer.exe      ← Double-click to run
├── index.html             ← Web interface
├── uploads/               ← Your uploaded PDFs
├── data/                  ← Document database
└── cache/                 ← Cached embeddings
```

That's it! No source code needed for normal use.

---

## For Developers: Source Code

### Essential Files

| File | Purpose |
|---|---|
| `main.py` | FastAPI backend (main logic) |
| `app_launcher.py` | PyInstaller entry point |
| `index.html` | Frontend UI |
| `requirements.txt` | Python dependencies |

### Build Scripts

| Script | Purpose |
|---|---|
| `setup.bat` | Install dependencies |
| `start.bat` | Run from source |
| `build_debug.bat` | Build .exe (quick) |
| `build_exe.bat` | Build .exe (full) |
| `prepare_release.bat` | Package for release |

### Development Setup

```bash
git clone https://github.com/ohm41321/Doc_Summary.git
cd Doc_Summary
setup.bat
start.bat
```

---

## Files Ignored by Git

These folders are **not** in the repository (created automatically):

- `uploads/` - User PDFs
- `data/` - SQLite database & FAISS indexes
- `cache/` - Embedding cache
- `venv/` - Python virtual environment
- `build/`, `dist/` - Build artifacts

---

**Need help?** See [README.md](README.md) or open an [Issue](https://github.com/ohm41321/Doc_Summary/issues)
