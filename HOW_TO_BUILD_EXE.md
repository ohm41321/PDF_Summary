# PDF Summarizer - สร้างเป็นไฟล์ .exe

## สิ่งที่ต้องทำ

ฉันได้สร้างไฟล์ที่จำเป็นสำหรับการแพ็กเกจแอปพลิเคชันเป็น .exe เรียบร้อยแล้ว:

### ไฟล์ที่สร้าง:
1. **main.spec** - PyInstaller specification file
2. **app_launcher.py** - ตัว launcher สำหรับเปิดแอปพร้อมเปิด browser อัตโนมัติ
3. **quick_build.bat** - สคริปต์สำหรับ build (แนะนำ)
4. **build_exe.bat** - สคริปต์ build แบบเดิม
5. **BUILD_INSTRUCTIONS.md** - คู่มือการ build
6. **hooks/hook-fitz.py** - PyInstaller hook สำหรับ PyMuPDF

## วิธี Build

### วิธีที่ 1: ง่ายที่สุด (แนะนำ)

```batch
quick_build.bat
```

### วิธีที่ 2: ใช้ build_exe.bat

```batch
build_exe.bat
```

### วิธีที่ 3: Build ด้วยตนเอง

```batch
# 1. เปิด Command Prompt ที่โฟลเดอร์โปรเจค
cd E:\SRC_CODE\Doc_Summary

# 2. เปิดใช้งาน virtual environment
venv\Scripts\activate.bat

# 3. ติดตั้ง PyInstaller (ถ้ายังไม่มี)
pip install pyinstaller

# 4. Build
pyinstaller ^
    --name PDFSummarizer ^
    --onedir ^
    --windowed ^
    --icon="E:\SRC_CODE\Doc_Summary\icon\lucia.ico" ^
    --add-data "index.html;." ^
    --add-data "main.py;." ^
    --hidden-import fitz ^
    --hidden-import PyMuPDF ^
    --hidden-import fastapi ^
    --hidden-import uvicorn ^
    --hidden-import easyocr ^
    --hidden-import faiss ^
    --collect-all fitz ^
    --collect-all fastapi ^
    --collect-all uvicorn ^
    --noconfirm ^
    app_launcher.py

# 5. สร้างโฟลเดอร์ที่จำเป็น
mkdir dist\PDFSummarizer\uploads
mkdir dist\PDFSummarizer\data
mkdir dist\PDFSummarizer\cache
```

## หลัง Build เสร็จ

โฟลเดอร์ `dist\PDFSummarizer\` จะมีไฟล์ดังนี้:
```
dist/PDFSummarizer/
├── PDFSummarizer.exe      ← ไฟล์หลัก (ดับเบิลคลิกเพื่อรัน)
├── index.html             ← หน้าเว็บ
├── uploads/               ← โฟลเดอร์เก็บ PDF
├── data/                  ← ฐานข้อมูล
├── cache/                 ← cache
└── ... (ไฟล์ .dll อื่นๆ)
```

## การใช้งาน

1. คัดลอกโฟลเดอร์ `dist\PDFSummarizer\` ทั้งหมดให้ผู้ใช้
2. ผู้ใช้แค่ดับเบิลคลิก `PDFSummarizer.exe`
3. **ไม่ต้องติดตั้ง Python!**
4. **ไม่ต้องติดตั้ง dependencies!**
5. แค่ต้องมี LM Studio รันอยู่ (ถ้าต้องการใช้ AI)

## หมายเหตุ

- ไฟล์ .exe จะมีขนาดใหญ่ (~300-800 MB) เพราะรวม Python และ dependencies ทั้งหมด
- ครั้งแรกที่เปิดอาจใช้เวลานาน เพราะ EasyOCR ต้องดาวน์โหลดโมเดลภาษาไทย
- ถ้า Windows Firewall เตือน ให้กด Allow

## ปัญหาที่อาจเจอ

### Build ไม่สำเร็จ
- ตรวจสอบว่า venv มีไลบรารีครบ: `pip install -r requirements.txt`
- ลองรัน: `pip install pyinstaller`

### รัน .exe แล้วไม่ขึ้น
- ตรวจสอบว่าไฟล์ `index.html` อยู่ในโฟลเดอร์เดียวกับ .exe
- ตรวจสอบว่าโฟลเดอร์ uploads, data, cache มีอยู่

### พอร์ต 8000 ถูกใช้
- ปิดโปรแกรมอื่นที่ใช้พอร์ต 8000 ก่อน
- หรือแก้ port ใน app_launcher.py

## การแก้ไขโค้ด

ถ้าต้องการแก้ไขโค้ด:
1. แก้ไขไฟล์ `main.py` หรือ `app_launcher.py`
2. รัน build script ใหม่
3. จะได้ .exe ใหม่ที่มีโค้ดล่าสุด
