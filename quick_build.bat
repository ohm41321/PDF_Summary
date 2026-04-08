@echo off
echo ============================================
echo   Quick Build PDF Summarizer
echo ============================================
echo.

REM Check virtual environment
if not exist "venv" (
    echo Error: venv folder not found!
    pause
    exit /b 1
)

if not exist "venv\Scripts\python.exe" (
    echo Error: Python executable not found in venv!
    pause
    exit /b 1
)

echo Using Python from: venv\Scripts\python.exe
venv\Scripts\python.exe --version
echo.

REM Install PyInstaller in venv if needed
echo Checking PyInstaller...
venv\Scripts\python.exe -m PyInstaller --version >nul 2>&1
if errorlevel 1 (
    echo Installing PyInstaller in venv...
    venv\Scripts\python.exe -m pip install pyinstaller
    if errorlevel 1 (
        echo Failed to install PyInstaller!
        pause
        exit /b 1
    )
)

echo.
echo Cleaning old builds...
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"

echo.
echo Building... (this will take several minutes)
echo.

REM Build using venv's Python explicitly
venv\Scripts\python.exe -m PyInstaller ^
    --name PDFSummarizer ^
    --onedir ^
    --console ^
    --icon="E:\SRC_CODE\Doc_Summary\icon\lucia.ico" ^
    --add-data "index.html;." ^
    --add-data "main.py;." ^
    --hidden-import fitz ^
    --hidden-import PyMuPDF ^
    --hidden-import pymupdf ^
    --hidden-import fastapi ^
    --hidden-import uvicorn ^
    --hidden-import easyocr ^
    --hidden-import faiss ^
    --hidden-import faiss.cpu ^
    --hidden-import PIL.Image ^
    --hidden-import PIL ^
    --hidden-import tiktoken ^
    --hidden-import numpy ^
    --hidden-import sqlite3 ^
    --hidden-import python_multipart ^
    --collect-all fitz ^
    --collect-all PyMuPDF ^
    --collect-all pymupdf ^
    --collect-all fastapi ^
    --collect-all uvicorn ^
    --collect-all pydantic ^
    --collect-all easyocr ^
    --collect-all faiss ^
    --collect-all PIL ^
    --collect-all scipy ^
    --exclude-module tkinter ^
    --exclude-module matplotlib ^
    --exclude-module jupyter ^
    --noconfirm ^
    app_launcher.py

if errorlevel 1 (
    echo.
    echo Build FAILED!
    pause
    exit /b 1
)

echo.
echo ============================================
echo   Build SUCCESS!
echo ============================================
echo.

REM Setup dist folder
if exist "dist\PDFSummarizer" (
    echo Setting up distribution folder...
    cd dist\PDFSummarizer

    if not exist "uploads" mkdir uploads
    if not exist "data" mkdir data
    if not exist "cache" mkdir cache
    if not exist "icon" mkdir icon

    cd ..\..

    echo.
    echo Application is ready at: dist\PDFSummarizer\PDFSummarizer.exe
    echo.
    echo To run: Double-click PDFSummarizer.exe
    echo.
)

pause
