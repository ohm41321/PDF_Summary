@echo off
echo ============================================
echo   Prepare for GitHub Upload
echo ============================================
echo.
echo This script will:
echo  1. Kill running processes
echo  2. Clean build artifacts
echo  3. Clean cache files (optional)
echo  4. Show final file list
echo.
pause

echo.
echo [1/4] Killing running processes...
taskkill /F /IM PDFSummarizer.exe 2>nul || echo   - No running instances

echo.
echo [2/4] Cleaning build artifacts...
if exist "build" (
    echo   Removing build/
    rmdir /s /q build 2>nul || echo   - Warning: Could not remove (files in use)
)
if exist "dist" (
    echo   Removing dist/
    rmdir /s /q dist 2>nul || echo   - Warning: Could not remove (files in use)
)
if exist "__pycache__" (
    echo   Removing __pycache__/
    rmdir /s /q __pycache__
)
del /q *.spec 2>nul
del /q server.log 2>nul
del /q *.pyc 2>nul

echo.
echo [3/4] Do you want to clean cache files?
echo   (This will remove embedding caches)
set /p CLEAN_CACHE="Clean cache? (y/N): "
if /i "%CLEAN_CACHE%"=="y" (
    if exist "cache" (
        echo   Removing cache/
        rmdir /s /q cache
        mkdir cache
        echo   - Cache cleaned
    )
) else (
    echo   - Cache preserved
)

echo.
echo [4/4] Final project structure:
echo ============================================
dir /b | findstr /v "venv" | findstr /v ".qwen"
echo ============================================

echo.
echo ✅ Project is ready for GitHub!
echo.
echo Next steps:
echo   1. git init
echo   2. git add .
echo   3. git commit -m "Initial commit"
echo   4. git remote add origin https://github.com/YOUR_USERNAME/Doc_Summary.git
echo   5. git push -u origin main
echo.
pause
