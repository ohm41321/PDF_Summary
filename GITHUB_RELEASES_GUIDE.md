# 📦 GitHub Releases Guide

**คู่มือการสร้างและเผยแพร่ .exe บน GitHub Releases**

---

## 🎯 เป้าหมาย

ทำให้ **users ดาวน์โหลด .exe ได้ง่ายๆ** โดยไม่ต้องติดตั้ง Python

---

## 📋 สิ่งที่ต้องมีก่อน

### ✅ เตรียมไว้แล้ว
- [x] Source code ทั้งหมด
- [x] Build scripts (`build_debug.bat`, `prepare_release.bat`)
- [x] README.md (เน้น .exe distribution)
- [x] LM_STUDIO_SETUP.md
- [x] .gitignore

### 🔧 ต้องทำก่อน Release
- [ ] Build .exe ให้สำเร็จ
- [ ] Test ว่า .exe ทำงานได้
- [ ] สร้าง ZIP file
- [ ] เขียน Release Notes

---

## 🚀 ขั้นตอนการสร้าง Release

### ขั้นตอนที่ 1: Build .exe

```bash
# เปิด Command Prompt ที่โฟลเดอร์โปรเจค
cd E:\SRC_CODE\Doc_Summary

# รันสคริปต์เตรียม Release
prepare_release.bat
```

**สคริปต์จะ:**
1. Kill process ที่รันอยู่
2. Build .exe (ถ้ายังไม่มี)
3. คัดลอกไฟล์ทั้งหมด
4. สร้าง `PDFSummarizer-v1.0.0-Windows.zip`

**ผลลัพธ์:**
```
✅ SUCCESS!
ไฟล์: PDFSummarizer-v1.0.0-Windows.zip
```

---

### ขั้นตอนที่ 2: Test .exe

1. แตกไฟล์ ZIP ที่สร้าง
2. รัน `PDFSummarizer.exe`
3. ตรวจสอบว่า:
   - ✅ เปิดได้
   - ✅ หน้าเว็บขึ้น
   - ✅ อัปโหลด PDF ได้
   - ✅ สรุปผลได้ (ถ้า LM Studio เปิดอยู่)

---

### ขั้นตอนที่ 3: สร้าง Git Tag

```bash
# สร้าง tag
git tag -a v1.0.0 -m "Version 1.0.0 - Initial Release"

# Push tag ขึ้น GitHub
git push origin v1.0.0
```

---

### ขั้นตอนที่ 4: สร้าง GitHub Release

#### วิธีที่ 1: ผ่านหน้าเว็บ (แนะนำ)

1. **เปิด:** https://github.com/ohm41321/Doc_Summary/releases/new

2. **กรอกข้อมูล:**
   - **Choose a tag:** `v1.0.0` (หรือสร้างใหม่)
   - **Release title:** `Version 1.0.0 - Initial Release`
   
3. **เขียน Description:**
```markdown
## 🎉 Initial Release

PDF Summarizer & Q&A - แอปสรุปเอกสารและถามตอบด้วย AI

### ✨ Features
- 📤 อัปโหลด PDF (drag & drop)
- 🤖 สรุปเอกสารอัตโนมัติ (สั้น + ละเอียด)
- 💬 ถามตอบเกี่ยวกับเอกสาร
- 🇹🇭 รองรับภาษาไทย-อังกฤษ
- 📥 Export สรุปและแชท
- 🚀 ไม่ต้องติดตั้ง Python

### 📥 ดาวน์โหลดและใช้งาน
1. ดาวน์โหลด ZIP
2. แตกไฟล์
3. ติดตั้ง LM Studio (https://lmstudio.ai/)
4. ดับเบิลคลิก PDFSummarizer.exe
5. เริ่มใช้งาน!

### 📖 คู่มือ
- วิธีใช้งาน: ดูใน README.md
- ตั้งค่า LM Studio: ดู LM_STUDIO_SETUP.md

### ⚙️ ความต้องการ
- Windows 10/11 (64-bit)
- RAM 8GB+
- LM Studio (สำหรับ AI features)

### 🐛 Known Issues
- ครั้งแรกที่เปิดอาจใช้เวลานาน (EasyOCR ดาวน์โหลดโมเดลภาษาไทย)
- ไฟล์ใหญ่ (>100 หน้า) ใช้เวลาประมวลผล 2-3 นาที

### 📝 หมายเหตุ
- ต้องเปิด LM Studio ทิ้งไว้ขณะใช้งาน
- ข้อมูลเก็บในเครื่อง (ไม่ส่ง cloud)
```

4. **แนบไฟล์:**
   - ลาก `PDFSummarizer-v1.0.0-Windows.zip` ใส่ **"Attach binaries"**

5. **ตรวจสอบ:**
   - ✅ ✅ This is a pre-release (ถ้ายัง beta)
   - ☑️ ✅ Set as the latest release (ถ้า stable)

6. **กด:** **"Publish release"**

---

#### วิธีที่ 2: ใช้ GitHub CLI

```bash
# สร้าง release
gh release create v1.0.0 \
  --title "Version 1.0.0 - Initial Release" \
  --notes-file RELEASE_NOTES.md \
  PDFSummarizer-v1.0.0-Windows.zip
```

---

### ขั้นตอนที่ 5: ตรวจสอบ

1. **เปิดหน้า Releases:** https://github.com/ohm41321/Doc_Summary/releases
2. **ตรวจสอบ:**
   - ✅ Release ขึ้นเป็น "Latest"
   - ✅ ไฟล์ ZIP แนบมา
   - ✅ Description แสดงถูกต้อง
   - ✅ Download link ทำงาน

---

## 📝 ตัวอย่าง Release Notes

### เวอร์ชัน 1.0.0 (Initial Release)

```markdown
## 🎉 Initial Release

PDF Summarizer & Q&A - แอปสรุปเอกสารและถามตอบด้วย AI

### ✨ Features
- 📤 อัปโหลด PDF (drag & drop, multiple files)
- 🤖 สรุปเอกสารอัตโนมัติ
  - Short summary (3-5 bullet points)
  - Detailed summary (comprehensive)
- 💬 ถามตอบเกี่ยวกับเอกสาร (AI-powered Q&A)
- 🇹🇭 รองรับภาษาไทย-อังกฤษ
- 📥 Export ผลลัพธ์
- 🚀 ไม่ต้องติดตั้ง Python
- 💾 Persistent storage

### 📥 Installation
1. ดาวน์โหลด ZIP
2. แตกไฟล์
3. ติดตั้ง LM Studio
4. ดับเบิลคลิก PDFSummarizer.exe

### ⚙️ Requirements
- Windows 10/11 (64-bit)
- RAM 8GB+
- LM Studio

### 🐛 Known Issues
- First run downloads EasyOCR models (~1-2 min)
- Large PDFs (>100 pages) take 2-3 minutes

### 🔜 Coming Soon
- [ ] Dark mode
- [ ] Batch processing
- [ ] Custom model config
```

---

### เวอร์ชัน 1.1.0 (ตัวอย่าง)

```markdown
## 🆕 What's New in v1.1.0

### ✨ New Features
- 🌙 Dark mode toggle
- 📊 Batch summary generation
- 🎨 Improved UI

### 🐛 Bug Fixes
- Fixed PDF upload issue for large files
- Fixed LM Studio connection timeout

### ⚡ Performance
- 30% faster processing
- Better memory management

### 📥 Download
Same as v1.0.0 - just replace the .exe file
```

---

## 🎨 Release Checklist

### ก่อนสร้าง Release

- [ ] Build .exe สำเร็จ
- [ ] Test .exe แล้ว (ทำงานได้)
- [ ] ZIP file สร้างแล้ว
- [ ] Release Notes เขียนแล้ว
- [ ] README อัพเดทเวอร์ชันแล้ว
- [ ] RELEASE_NOTES.md เพิ่ม entry ใหม่แล้ว

### ระหว่างสร้าง Release

- [ ] Tag ถูกต้อง (v1.0.0)
- [ ] Title ชัดเจน
- [ ] Description ครบถ้วน
- [ ] ZIP file แนบแล้ว
- [ ] ตรวจสอบ links ทั้งหมด

### หลังสร้าง Release

- [ ] เปิดหน้า Release ได้
- [ ] Download link ทำงาน
- [ ] Description แสดงถูกต้อง
- [ ] ขึ้นเป็น "Latest release"
- [ ] แจ้งผู้ใช้ (ถ้ามี)

---

## 🔄 วิธีอัพเดท Release

### Minor Update (v1.0.0 → v1.0.1)

```bash
# 1. แก้ไขโค้ด
# 2. Build ใหม่
prepare_release.bat

# 3. สร้าง tag ใหม่
git tag -a v1.0.1 -m "Version 1.0.1 - Bug fixes"
git push origin v1.0.1

# 4. สร้าง release ใหม่
# (ทำเหมือน v1.0.0)
```

### Major Update (v1.0.0 → v2.0.0)

```bash
# 1. เพิ่มฟีเจอร์ใหญ่
# 2. อัพเดท README
# 3. Build ใหม่
prepare_release.bat

# 4. สร้าง tag ใหม่
git tag -a v2.0.0 -m "Version 2.0.0 - Major update"
git push origin v2.0.0

# 5. สร้าง release ใหม่
```

---

## 💡 Tips

### ทำให้ Release น่าสนใจ

1. **ใช้ Emoji** ใน description
2. **มี screenshots** ของแอป
3. **เขียน changelog** ชัดเจน
4. **บอกวิธีอัพเกรด** จากเวอร์ชันเก่า

### ทำให้ดาวน์โหลดง่าย

1. **ตั้งชื่อไฟล์ชัดเจน:**
   - ✅ `PDFSummarizer-v1.0.0-Windows.zip`
   - ❌ `release.zip`

2. **เขียนวิธีติดตั้งสั้นๆ:**
   ```
   1. แตกไฟล์ ZIP
   2. ดับเบิลคลิก PDFSummarizer.exe
   3. ใช้งาน!
   ```

3. **บอกความต้องการระบบ:**
   - Windows 10/11
   - RAM 8GB+
   - LM Studio

### โปรโมท Release

1. **Share on social:**
   - Twitter/X
   - Facebook groups
   - Reddit (r/Python, r/MachineLearning)
   - Thai developer communities

2. **สร้าง YouTube video:**
   - สอนวิธีติดตั้ง
   - สาธิตการใช้งาน
   - ลิงก์ไปที่ Releases

---

## 🐛 ปัญหาที่พบบ่อย

### Release ไม่ขึ้นเป็น "Latest"

**แก้:** Edit release → ✅ "Set as the latest release"

### ไฟล์ ZIP ไม่แนบ

**แก้:** Edit release → ลากไฟล์ใส่ "Attach binaries" อีกครั้ง

### Tag ซ้ำ

**แก้:** ใช้ tag ใหม่ (v1.0.1) หรือลบ tag เก่า:
```bash
git tag -d v1.0.0
git push --delete origin v1.0.0
```

### Upload ล้มเหลว

**แก้:**
- ตรวจสอบขนาดไฟล์ (GitHub จำกัด 2GB ต่อไฟล์)
- ลองอัพโหลดใหม่
- ใช้ GitHub CLI แทน

---

## 📊 ตัวอย่างโครงสร้าง Releases

```
Releases
├── v1.0.0 (Latest) - April 2026
│   └── PDFSummarizer-v1.0.0-Windows.zip (800 MB)
│
├── v0.9.0 (Beta) - March 2026
│   └── PDFSummarizer-v0.9.0-Beta-Windows.zip
│
└── v0.1.0 (Alpha) - February 2026
    └── PDFSummarizer-v0.1.0-Alpha.zip
```

---

## ✅ Release สำเร็จ!

เมื่อทำครบทุกขั้นตอน:

1. ✅ Users ดาวน์โหลด .exe ได้จาก Releases
2. ✅ ไม่ต้องติดตั้ง Python
3. ✅ แค่มี Windows + LM Studio
4. ✅ ดับเบิลคลิกแล้วใช้งานได้เลย!

---

**พร้อมแล้ว! รัน `prepare_release.bat` แล้วสร้าง Release แรกเลย!** 🚀
