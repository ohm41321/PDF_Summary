@echo off
echo ============================================
echo   Building PDF Summarizer to .exe
echo ============================================
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Virtual environment not found!
    echo Please run setup.bat first.
    pause
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Check if PyInstaller is installed
pyinstaller --version >nul 2>&1
if errorlevel 1 (
    echo Installing PyInstaller...
    pip install pyinstaller
    if errorlevel 1 (
        echo Failed to install PyInstaller!
        pause
        exit /b 1
    )
)

echo.
echo Cleaning previous builds...
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"

echo.
echo Building executable...
echo This may take several minutes...
echo.

REM Build using the spec file
pyinstaller main.spec --clean

if errorlevel 1 (
    echo.
    echo Build failed! Check the error messages above.
    pause
    exit /b 1
)

echo.
echo ============================================
echo   Build completed successfully!
echo ============================================
echo.
echo The executable is located in:
echo   dist\PDFSummarizer\PDFSummarizer.exe
echo.
echo IMPORTANT: You must also copy the following folders to the dist directory:
echo   - uploads
echo   - data
echo   - cache
echo   - index.html
echo.
echo Creating setup package...
echo.

REM Create the complete distribution package
if exist "dist\PDFSummarizer" (
    REM Copy required files to the dist folder
    if exist "index.html" copy /Y "index.html" "dist\PDFSummarizer\" >nul
    if not exist "dist\PDFSummarizer\uploads" mkdir "dist\PDFSummarizer\uploads"
    if not exist "dist\PDFSummarizer\data" mkdir "dist\PDFSummarizer\data"
    if not exist "dist\PDFSummarizer\cache" mkdir "dist\PDFSummarizer\cache"
    if not exist "dist\PDFSummarizer\icon" mkdir "dist\PDFSummarizer\icon"
    
    echo Distribution package created at:
    echo   dist\PDFSummarizer\
    echo.
    echo To run the application:
    echo   1. Navigate to dist\PDFSummarizer
    echo   2. Double-click PDFSummarizer.exe
    echo.
)

echo ============================================
echo   Build Process Complete!
echo ============================================
echo.
pause
