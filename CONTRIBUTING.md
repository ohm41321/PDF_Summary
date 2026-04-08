# Contributing to PDF Summarizer & Q&A

Thank you for your interest in contributing! This guide will help you get started.

---

## 🚀 Quick Start for Contributors

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/Doc_Summary.git`
3. Create a branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Test your changes
6. Commit: `git commit -m "feat: add your feature"`
7. Push: `git push origin feature/your-feature-name`
8. Open a Pull Request

---

## 📋 Development Setup

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git

### Initial Setup

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/Doc_Summary.git
cd Doc_Summary

# Run automated setup
setup.bat

# Or manual setup:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Run the application
start.bat
# Or: python main.py
```

### Building the .exe

```bash
# Quick build (for testing)
build_debug.bat

# Full build (for release)
build_exe.bat
```

---

## 📝 Code Style Guidelines

### Python Code

- Follow PEP 8 style guide
- Use type hints where possible
- Add docstrings to functions and classes
- Keep functions focused and under 50 lines when possible
- Use meaningful variable names

Example:
```python
def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract text content from PDF file.
    
    Args:
        file_path: Path to the PDF file
        
    Returns:
        Extracted text content
    """
    # Implementation
```

### Frontend (HTML/JS/CSS)

- Use semantic HTML
- Keep JavaScript modular (functions under 30 lines)
- Use consistent naming conventions (camelCase for JS, kebab-case for CSS)
- Comment complex logic

### Commit Messages

Follow conventional commits format:

```
type: description

Examples:
feat: add Thai language support
fix: resolve PDF upload timeout issue
docs: update README with LM Studio guide
refactor: optimize embedding caching
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting changes
- `refactor`: Code restructuring
- `perf`: Performance improvements
- `test`: Test additions/updates
- `chore`: Maintenance tasks

---

## 🧪 Testing

Before submitting a PR:

1. **Run the application** from source
   ```bash
   start.bat
   ```

2. **Test core features:**
   - Upload a PDF
   - Generate summaries
   - Ask questions
   - Switch languages

3. **Build the .exe** (if making backend changes)
   ```bash
   build_debug.bat
   ```

4. **Test the .exe** to ensure it works

---

## 📂 Project Structure

```
Doc_Summary/
├── main.py                 # FastAPI backend (core logic)
├── app_launcher.py         # PyInstaller entry point
├── index.html              # Frontend interface
├── requirements.txt        # Python dependencies
│
├── setup.bat              # Automated setup script
├── start.bat              # Quick start script
├── build_debug.bat        # Build .exe (debug)
├── build_exe.bat          # Build .exe (production)
├── prepare_release.bat    # Package for release
│
├── README.md              # Main documentation (.exe first)
├── REPO_STRUCTURE.md      # Repository layout guide
├── RELEASE_NOTES.md       # Version history
├── CONTRIBUTING.md        # This file
├── LICENSE                # MIT License
└── .gitignore             # Git ignore rules
```

---

## 🔍 Pull Request Guidelines

### Before Submitting

- [ ] Code follows style guidelines
- [ ] Tested locally
- [ ] Commit messages are clear
- [ ] No unnecessary files (uploads/, data/, cache/, venv/)
- [ ] Branch is up to date with main

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tested from source
- [ ] Tested .exe build
- [ ] All features work as expected

## Screenshots (if applicable)
Add screenshots showing the changes
```

---

## 🐛 Reporting Issues

Use the issue templates:

- **Bug Report**: For bugs and problems
- **Feature Request**: For new ideas

Include:
- Clear description
- Steps to reproduce (for bugs)
- Expected vs actual behavior
- System information

---

## 📚 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [PyInstaller Documentation](https://pyinstaller.org/)
- [LM Studio API](https://lmstudio.ai/docs/api)
- [FAISS Documentation](https://faiss.ai/)

---

## ❓ Questions?

- Open a [Discussion](https://github.com/ohm41321/Doc_Summary/discussions)
- Or ask in an [Issue](https://github.com/ohm41321/Doc_Summary/issues)

---

Thank you for contributing! 🎉
