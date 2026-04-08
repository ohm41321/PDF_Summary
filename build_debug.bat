@echo off
echo ============================================
echo   Minimal Build (Debug Mode)
echo ============================================
echo.

if not exist "venv\Scripts\python.exe" (
    echo Error: venv not found!
    pause
    exit /b 1
)

echo Installing PyInstaller in venv...
venv\Scripts\python.exe -m pip install pyinstaller -q

echo.
echo Cleaning old builds...
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"

echo.
echo Building... (please wait 3-5 minutes)
echo.

venv\Scripts\python.exe -m PyInstaller ^
    --name PDFSummarizer ^
    --onedir ^
    --console ^
    --add-data "index.html;." ^
    --hidden-import fitz ^
    --hidden-import PyMuPDF ^
    --hidden-import fastapi ^
    --hidden-import uvicorn ^
    --hidden-import easyocr ^
    --hidden-import faiss ^
    --hidden-import PIL ^
    --hidden-import scipy ^
    --hidden-import numpy ^
    --hidden-import tiktoken ^
    --hidden-import python_multipart ^
    --collect-all easyocr ^
    --collect-all faiss ^
    --collect-all scipy ^
    --exclude-module tkinter ^
    --exclude-module matplotlib ^
    --noconfirm ^
    app_launcher.py

if errorlevel 1 (
    echo.
    echo BUILD FAILED!
    pause
    exit /b 1
)

echo.
echo ============================================
echo   Build SUCCESS!
echo ============================================
echo.

if exist "dist\PDFSummarizer" (
    cd dist\PDFSummarizer
    if not exist "uploads" mkdir uploads
    if not exist "data" mkdir data
    if not exist "cache" mkdir cache
    cd ..\..

    echo.
    Ready to run: dist\PDFSummarizer\PDFSummarizer.exe
    echo.
)

pause
