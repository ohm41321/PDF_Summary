# 🔧 LM Studio Setup Guide

Quick setup guide for using LM Studio with PDF Summarizer.

---

## 📥 1. Download & Install LM Studio

🔗 **https://lmstudio.ai/**

- Free for personal use
- Windows, Mac, Linux support

---

## 📦 2. Download Models

You need **two types** of models:

| Type | Purpose | Recommended |
|---|---|---|
| **LLM** | Summaries & Q&A | Typhoon-v1.5x-7B (Thai) or Qwen2.5-7B (Mixed) |
| **Embedding** | Document search | bge-m3 (Multilingual) |

### Quick Download Steps

1. Open LM Studio → Click **🔍 Search** tab
2. Search for model name
3. Click **Download** (Q4_K_M version recommended)
4. Wait for download to complete

### ⭐ Recommended Models

**For Thai Documents:**
- LLM: `Typhoon-v1.5x-7B` 🇹🇭
- Embedding: `bge-m3`

**For Mixed Thai-English:**
- LLM: `Qwen2.5-7B-Instruct`
- Embedding: `bge-m3`

---

## 🖥️ 3. Start Server

1. Go to **🖥️ Local Server** tab
2. Select your downloaded LLM model
3. Click **"Start Server"**
4. Wait for green indicator ✅

---

## 🎯 4. Run PDF Summarizer

1. Start LM Studio server first
2. Run `PDFSummarizer.exe`
3. App auto-detects LM Studio at `http://localhost:1234`
4. Check green status dot (top-right) = Connected!

---

## ❓ Troubleshooting

| Problem | Solution |
|---|---|
| **Can't connect** | ✓ Check LM Studio is running<br/>✓ Server started (green indicator) |
| **No response** | ✓ Verify model fully downloaded<br/>✓ Try simpler question |
| **Out of memory** | ✓ Use Q4_K_M quantization<br/>✓ Close other apps |
| **Poor Thai quality** | ✓ Switch to Typhoon model<br/>✓ Check embedding model is loaded |

---

## 💡 Pro Tips

- **Q4_K_M quantization**: Best quality/speed balance
- **Enable GPU offload**: If you have NVIDIA GPU
- **Close other apps**: Frees up RAM (important for 8GB systems)
- **First run slower**: Embeddings cache for faster subsequent runs

---

**Full guide with detailed model comparisons:** See the expanded guide in the repository or visit [LM Studio Docs](https://lmstudio.ai/docs)

