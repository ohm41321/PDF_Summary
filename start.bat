@echo off
echo ============================================
echo   Starting PDF Summarizer Server
echo ============================================
echo.

if not exist "venv" (
    echo Virtual environment not found! Running setup first...
    call setup.bat
)

call venv\Scripts\activate.bat

echo Starting server...
echo.

:: Start server in background, capture PID
start /b python main.py > server.log 2>&1
set PID=%ERRORLEVEL%

echo Waiting for server to be ready...

:: Poll until server responds
for /l %%i in (1,1,30) do (
    timeout /t 1 /nobreak >nul
    curl -s http://localhost:8000/health >nul 2>&1
    if not errorlevel 1 (
        echo.
        echo Server is ready!
        echo Opening browser...
        start http://localhost:8000
        goto :running
    )
    echo   Waiting... %%i/30
)

echo.
echo [!] Server did not start within 30 seconds.
echo [!] Check server.log for errors.
echo.
pause
exit /b 1

:running
echo.
echo Server running at http://localhost:8000
echo.
pause
