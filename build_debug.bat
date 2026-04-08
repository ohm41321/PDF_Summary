@echo off
echo ============================================
echo   Build PDF Summarizer to .exe
echo ============================================
echo.

if not exist "venv\Scripts\python.exe" (
    echo Error: venv not found!
    echo Run setup.bat first.
    pause
    exit /b 1
)

echo Using Python: venv\Scripts\python.exe
venv\Scripts\python.exe --version
echo.

REM Install PyInstaller
echo Checking PyInstaller...
venv\Scripts\python.exe -m PyInstaller --version >nul 2>&1
if errorlevel 1 (
    echo Installing PyInstaller...
    venv\Scripts\python.exe -m pip install pyinstaller -q
)

echo.
echo Cleaning old builds...
taskkill /F /IM PDFSummarizer.exe 2>nul
timeout /t 2 /nobreak >nul
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"

echo.
echo Building... (3-5 minutes)
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
    --collect-all PIL ^
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

    echo Ready: dist\PDFSummarizer\PDFSummarizer.exe
    echo.
)

pause
