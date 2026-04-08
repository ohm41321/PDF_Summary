# Building PDF Summarizer to .exe

This guide explains how to build the PDF Summarizer application into a standalone .exe file.

## Prerequisites

1. **Python 3.10+** must be installed on your system
2. All dependencies from `requirements.txt` must be installed
3. You must have a working internet connection (for downloading PyInstaller)

## Build Instructions

### Option 1: Automated Build (Recommended)

1. Open Command Prompt in the project directory
2. Run the build script:
   ```batch
   build_exe.bat
   ```

3. Wait for the build to complete (this may take 5-10 minutes)
4. The built application will be in the `dist\PDFSummarizer\` folder

### Option 2: Manual Build

If you prefer to build manually:

```batch
# Activate virtual environment
venv\Scripts\activate.bat

# Install PyInstaller (if not already installed)
pip install pyinstaller

# Build the application
pyinstaller main.spec

# Copy required files to dist folder
copy index.html dist\PDFSummarizer\
mkdir dist\PDFSummarizer\uploads
mkdir dist\PDFSummarizer\data
mkdir dist\PDFSummarizer\cache
```

## Distribution

After building, you can distribute the entire `dist\PDFSummarizer\` folder to users. The folder contains:

- `PDFSummarizer.exe` - The main application
- `uploads/` - Directory for uploaded PDFs
- `data/` - Database and index files
- `cache/` - Embedding cache
- `index.html` - Frontend interface
- Various `.dll` and support files

**Important:** Users do NOT need to install Python or any dependencies. Everything is packaged.

## Running the Application

1. Navigate to `dist\PDFSummarizer\`
2. Double-click `PDFSummarizer.exe`
3. The application will automatically:
   - Start the local server
   - Open your web browser to http://localhost:8000

## Notes

- **First Run**: The first startup may take longer as EasyOCR downloads language models
- **LM Studio**: You still need LM Studio running for the AI features to work
- **Firewall**: Windows may ask for firewall permissions - allow access for the app to work properly

## Troubleshooting

### Build fails with "Module not found"
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Run: `pip install pyinstaller`

### Build is too large
- The build includes all dependencies, so it will be large (~500MB-1GB)
- This is normal and expected

### Application doesn't start
- Check if port 8000 is already in use
- Make sure LM Studio is running (for AI features)
- Check Windows Firewall settings

### "index.html not found" error
- Make sure `index.html` is in the same folder as `PDFSummarizer.exe`
- The entire `dist\PDFSummarizer\` folder must be kept together

## For Developers

To modify what gets included in the build, edit `main.spec`:
- Add more files to the `datas` list
- Add more modules to `hiddenimports` if needed
- Change `console=False` to `console=True` to see console output (useful for debugging)
