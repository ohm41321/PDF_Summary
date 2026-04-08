@echo off
echo ============================================
echo   Prepare Release for GitHub
echo ============================================
echo.
echo This script will:
echo   1. Kill running processes
echo   2. Build .exe (if not exists)
echo   3. Create release package
echo   4. Create ZIP file for GitHub Releases
echo.
pause

echo.
echo [1/4] Killing running processes...
taskkill /F /IM PDFSummarizer.exe 2>nul || echo   - No running instances

echo.
echo [2/4] Building .exe...
if not exist "dist\PDFSummarizer\PDFSummarizer.exe" (
    echo Build not found! Running build...
    echo.
    call build_debug.bat
    if errorlevel 1 (
        echo.
        echo Build failed!
        pause
        exit /b 1
    )
) else (
    echo   - Build already exists
)

echo.
echo [3/4] Creating release package...
if exist "release_package" rmdir /s /q release_package
mkdir release_package
mkdir release_package\PDFSummarizer

echo Copying application files...
xcopy "dist\PDFSummarizer\*.*" "release_package\PDFSummarizer\" /E /I /Y /Q >nul

(
echo PDF Summarizer ^& Q&A v1.0.0
echo ========================================
echo.
echo วิธีใช้งาน
echo ----------
echo 1. แตกไฟล์ ZIP
echo 2. ติดตั้ง LM Studio: https://lmstudio.ai/
echo 3. เปิด LM Studio ^> Download Model ^> Start Server
echo 4. ดับเบิลคลิก PDFSummarizer.exe
echo 5. อัปโหลด PDF ^& ใช้งาน!
echo.
echo แนะนำโมเดล
echo ----------
echo LLM:
echo   - Typhoon-v1.5x-7B (ไทยดีที่สุด)
echo   - Qwen2.5-7B-Instruct (ดีทั้งไทย+อังกฤษ)
echo.
echo Embedding:
echo   - bge-m3 (ดีที่สุด)
echo   - BAAI/bge-base-th (เฉพาะไทย)
echo.
echo ต้องการความช่วยเหลือ?
echo --------------------
echo คู่มือ: LM_STUDIO_SETUP.md
echo รายงานปัญหา: https://github.com/ohm41321/Doc_Summary/issues
echo.
echo พัฒนาโดย ItsAthtz
) > "release_package\PDFSummarizer\README.txt"

echo.
echo [4/4] Creating ZIP file...
powershell -Command "Compress-Archive -Path 'release_package\PDFSummarizer' -DestinationPath 'PDFSummarizer-v1.0.0-Windows.zip' -Force" >nul

if exist "PDFSummarizer-v1.0.0-Windows.zip" (
    echo.
    echo ============================================
    echo   ✅ SUCCESS!
    echo ============================================
    echo.
    echo ไฟล์พร้อมอัพขึ้น GitHub Releases:
    echo.
    for %%A in ("PDFSummarizer-v1.0.0-Windows.zip") do echo ชื่อ: %%~nxA
    for %%A in ("PDFSummarizer-v1.0.0-Windows.zip") do echo ขนาด: %%~zA bytes
    echo.
    echo ขั้นตอนต่อไป:
    echo   1. ไปที่: https://github.com/ohm41321/Doc_Summary/releases/new
    echo   2. Tag version: v1.0.0
    echo   3. Release title: Version 1.0.0 - Initial Release
    echo   4. ลากไฟล์ ZIP ใส่ "Attach binaries"
    echo   5. กด "Publish release"
    echo.
    
    rmdir /s /q release_package
) else (
    echo.
    echo ❌ Failed to create ZIP!
    pause
    exit /b 1
)

pause
