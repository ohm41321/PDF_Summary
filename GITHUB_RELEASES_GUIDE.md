# 📦 GitHub Releases Guide

Guide for building and publishing releases to GitHub.

---

## 🎯 Purpose

Enable **users to download .exe directly** without Python installation.

---

## 📋 Prerequisites

- [x] All source code ready
- [x] Build scripts available (`build_debug.bat`, `prepare_release.bat`)
- [ ] .exe built and tested
- [ ] Release notes written

---

## 🚀 Build & Release Steps

### Step 1: Build .exe

```bash
prepare_release.bat
```

This script will:
1. Kill running processes
2. Build .exe if needed
3. Copy all necessary files
4. Create `PDFSummarizer-vX.X.X-Windows.zip`

### Step 2: Test the .exe

1. Extract the ZIP
2. Run `PDFSummarizer.exe`
3. Verify it works (upload, summarize, Q&A)

### Step 3: Create Git Tag & Push

```bash
git tag -a v1.0.0 -m "Version 1.0.0 - Initial Release"
git push origin v1.0.0
```

### Step 4: Create GitHub Release

1. Go to: https://github.com/ohm41321/Doc_Summary/releases/new
2. Select tag: `v1.0.0`
3. Title: `Version 1.0.0 - Initial Release`
4. Write description (see template below)
5. Attach ZIP file: Drag `PDFSummarizer-v1.0.0-Windows.zip`
6. Check "Set as the latest release"
7. Click **"Publish release"**

---

## 📝 Release Notes Template

```markdown
## 🎉 Initial Release

PDF Summarizer & Q&A - AI-powered PDF analysis tool

### ✨ Features
- 📤 PDF Upload (drag & drop, multiple files)
- 🤖 Auto summarization (short + detailed)
- 💬 Smart Q&A based on document content
- 🇹🇭 Thai-English multilingual support
- 📥 Export summaries and chat history
- 🚀 No Python installation required

### 📥 Quick Start
1. Download ZIP
2. Extract files
3. Install LM Studio (https://lmstudio.ai/)
4. Double-click PDFSummarizer.exe
5. Start using!

### ⚙️ Requirements
- Windows 10/11 (64-bit)
- RAM 8GB+
- LM Studio running

### 🐛 Known Issues
- First run may be slower (EasyOCR model download)
- Large PDFs (>100 pages) take 2-3 minutes to process

### 📖 Documentation
- Usage guide: See README.md
- LM Studio setup: See LM_STUDIO_SETUP.md
```

---

## 🔄 Version Updates

### Minor Update (v1.0.0 → v1.0.1)

```bash
# Make changes, build, tag, push
prepare_release.bat
git tag -a v1.0.1 -m "Version 1.0.1 - Bug fixes"
git push origin v1.0.1
# Create new release on GitHub
```

### Major Update (v1.0.0 → v2.0.0)

```bash
# Major feature changes, update README
prepare_release.bat
git tag -a v2.0.0 -m "Version 2.0.0 - Major update"
git push origin v2.0.0
# Create new release on GitHub
```

---

## 💡 Best Practices

1. **Clear file naming:** `PDFSummarizer-vX.X.X-Windows.zip`
2. **Include version in README**
3. **Write detailed release notes**
4. **Test .exe before publishing**
5. **Update RELEASE_NOTES.md**

---

## ❓ Troubleshooting

| Problem | Solution |
|---|---|
| **Release not "Latest"** | Edit → Check "Set as latest release" |
| **ZIP not attaching** | Drag file again to "Attach binaries" |
| **Tag conflict** | Use new tag or delete old: `git tag -d v1.0.0` |
| **Upload fails** | Check file size (<2GB), retry |

---

**Ready to release?** Run `prepare_release.bat` and follow the steps! 🚀

