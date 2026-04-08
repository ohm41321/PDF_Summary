@echo off
echo ============================================
echo   PDF Summarizer - Setup
echo ============================================
echo.

:: Check Python
echo [1/5] Checking Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python not found - Installing automatically...
    echo.
    echo [!] Downloading Python...
    
    :: Download Python installer
    powershell -Command "& {Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe' -OutFile '%%TEMP%%\python-installer.exe'}"
    
    echo [!] Installing Python... (may take 2-5 minutes)
    echo [!] Please wait...
    
    :: Install Python silently
    %%TEMP%%\python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_pip=1
    
    :: Clean up
    del %%TEMP%%\python-installer.exe >nul 2>&1
    
    echo [OK] Python installed!
    echo.
) else (
    echo [OK] Python found!
)

echo.
echo [2/5] Creating virtual environment...
if not exist "venv" (
    python -m venv venv
    echo [OK] Virtual environment created!
) else (
    echo [OK] Virtual environment exists!
)

echo.
echo [3/5] Installing dependencies...
call venv\Scripts\activate.bat
pip install -r requirements.txt --quiet
if %errorlevel% neq 0 (
    echo [!] Error installing dependencies!
    pause
    exit /b 1
)
echo [OK] Dependencies installed!

echo.
echo [4/5] Creating folders...
if not exist "uploads" mkdir uploads
if not exist "data" mkdir data
echo [OK] Folders created!

echo.
echo [5/5] Checking LM Studio...
python check_lmstudio.py 2>nul

echo.
echo ============================================
echo   Setup Complete!
echo ============================================
echo.
echo Next steps:
echo 1. Open LM Studio and Start Server
echo 2. Double-click: start.bat
echo.
pause
