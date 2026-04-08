# 📦 GitHub Repository Structure Guide

## โครงสร้าง Repository

Repository นี้มี **2 ส่วน**:

### 1️⃣ สำหรับ Users (ดาวน์โหลด .exe)

**ไปที่:** [Releases](../../releases) → ดาวน์โหลดเวอร์ชันล่าสุด

**ไม่ต้องติดตั้งอะไรเพิ่ม:**
- ✅ แค่ Windows 10/11
- ✅ RAM 8GB+
- ✅ LM Studio (สำหรับ AI)

### 2️⃣ สำหรับ Developers (Source Code)

**Clone repo นี้:**
```bash
git clone https://github.com/ohm41321/Doc_Summary.git
```

**Build เอง:**
```bash
setup.bat          # ติดตั้ง dependencies
build_debug.bat    # Build เป็น .exe
```

---

## 📁 โครงสร้างไฟล์

```
Doc_Summary/
│
├── 📄 สำหรับ Users
│   ├── README.md                    ← คู่มือหลัก (เน้น .exe)
│   ├── LM_STUDIO_SETUP.md           ← คู่มือ LM Studio
│   ├── RELEASE_NOTES.md             ← ประวัติเวอร์ชัน
│   └── prepare_release.bat          ← สคริปต์เตรียม Release
│
├── 💻 สำหรับ Developers
│   ├── main.py                      ← Backend (FastAPI)
│   ├── app_launcher.py              ← Entry point สำหรับ PyInstaller
│   ├── index.html                   ← Frontend
│   ├── requirements.txt             ← Python dependencies
│   ├── setup.bat                    ← ติดตั้ง dependencies
│   ├── start.bat                    ← รันแอปจาก source
│   ├── build_debug.bat              ← Build .exe (debug)
│   ├── build_exe.bat                ← Build .exe (full)
│   ├── quick_build.bat              ← Build .exe (quick)
│   ├── main.spec                    ← PyInstaller spec
│   ├── check_lmstudio.py            ← ตรวจสอบ LM Studio
│   └── hooks/                       ← PyInstaller hooks
│
└── 📁 อื่นๆ
    ├── .gitignore                   ← Git ignore rules
    ├── LICENSE                      ← MIT License
    ├── icon/                        ← Application icon
    ├── uploads/                     ← Uploaded PDFs (git ignored)
    ├── data/                        ← Database (git ignored)
    ├── cache/                       ← Cache (git ignored)
    └── release_package/             ← Temporary (created by prepare_release.bat)
```

---

## 🎯 สำหรับ Users: วิธีดาวน์โหลด .exe

### ขั้นตอนที่ 1: ไปที่ Releases

เปิด: https://github.com/ohm41321/Doc_Summary/releases

### ขั้นตอนที่ 2: ดาวน์โหลด

- คลิกเวอร์ชันล่าสุด (เช่น v1.0.0)
- ดาวน์โหลดไฟล์ ZIP (เช่น `PDFSummarizer-v1.0.0-Windows.zip`)

### ขั้นตอนที่ 3: ใช้งาน

1. แตกไฟล์ ZIP
2. ดับเบิลคลิก `PDFSummarizer.exe`
3. เริ่มใช้งาน!

---

## 🔧 สำหรับ Developers: วิธี Build เอง

### Setup

```bash
# 1. Clone repo
git clone https://github.com/ohm41321/Doc_Summary.git
cd Doc_Summary

# 2. ติดตั้ง dependencies
setup.bat

# 3. รันแอป
start.bat
```

### Build .exe

```bash
# วิธีที่ 1: ง่ายสุด (แนะนำ)
build_debug.bat

# วิธีที่ 2: Full build
build_exe.bat

# วิธีที่ 3: Quick build
quick_build.bat
```

### Prepare Release

```bash
# สร้าง ZIP สำหรับอัพขึ้น GitHub Releases
prepare_release.bat
```

---

## 📦 วิธีสร้าง Release ใหม่

### 1. อัพเดทเวอร์ชัน

แก้ไขไฟล์เหล่านี้:
- `README.md` - อัพเดท version number
- `RELEASE_NOTES.md` - เพิ่ม release notes

### 2. Build .exe

```bash
prepare_release.bat
```

จะได้ไฟล์: `PDFSummarizer-vX.X.X-Windows.zip`

### 3. สร้าง Git Tag

```bash
git tag -a v1.0.0 -m "Version 1.0.0 - Initial Release"
git push origin v1.0.0
```

### 4. สร้าง GitHub Release

1. ไปที่: https://github.com/ohm41321/Doc_Summary/releases/new
2. Tag version: `v1.0.0`
3. Release title: `Version 1.0.0 - Initial Release`
4. Description: คัดลอกจาก RELEASE_NOTES.md
5. Attach binaries: ลากไฟล์ ZIP ใส่
6. กด **"Publish release"**

---

## 🚀 Git Commands สำหรับเริ่มต้น

```bash
# Clone repo
git clone https://github.com/ohm41321/Doc_Summary.git
cd Doc_Summary

# ดูสถานะ
git status

# เพิ่มไฟล์
git add .

# Commit
git commit -m "Initial commit"

# Push
git push origin main

# สร้าง tag สำหรับ release
git tag -a v1.0.0 -m "Version 1.0.0"
git push origin v1.0.0
```

---

## ⚠️ ไฟล์ที่ไม่ควรอัพขึ้น Git

ไฟล์เหล่านี้ถูกกันไว้ด้วย `.gitignore`:

- ❌ `venv/` - Virtual environment (ใหญ่เกินไป)
- ❌ `uploads/` - ผู้ใช้ PDFs
- ❌ `data/` - ฐานข้อมูล
- ❌ `cache/` - แคช
- ❌ `build/` - Build artifacts
- ❌ `dist/` - Compiled binaries
- ❌ `release_package/` - Temporary files
- ❌ `*.zip` - Release packages

---

## 📝 Commit Message Guidelines

```bash
# Features
git commit -m "feat: add Thai language support"

# Bug fixes
git commit -m "fix: resolve PDF upload issue"

# Documentation
git commit -m "docs: update README with LM Studio guide"

# Releases
git commit -m "release: v1.0.0 - Initial release"
```

---

## 🤝 Contributing

1. Fork repo
2. Create branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'feat: add amazing feature'`)
4. Push (`git push origin feature/amazing-feature`)
5. เปิด Pull Request

---

**มีคำถาม?** เปิด Issue: https://github.com/ohm41321/Doc_Summary/issues
