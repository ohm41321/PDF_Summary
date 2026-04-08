# 🔧 LM Studio Setup Guide

**Complete guide for setting up LM Studio with PDF Summarizer**

---

## 📥 Step 1: Download LM Studio

### Official Download
🔗 **https://lmstudio.ai/**

- Supports Windows, Mac, Linux
- Free for personal use
- No registration required

---

## 🚀 Step 2: Install & Launch

### Windows Installation
1. Download the `.exe` installer
2. Run the installer
3. Follow the setup wizard
4. Launch LM Studio

### First Launch
- LM Studio will initialize
- You'll see the main interface with tabs:
  - 🔍 **Search** - Download models
  - 💬 **Chat** - Test models
  - 🖥️ **Local Server** - Start API server

---

## 📦 Step 3: Download Models

### Understanding Model Types

| Type | Purpose | Used For |
|---|---|---|
| **LLM (Chat Model)** | Chat, summarization, Q&A | Generating summaries, answering questions |
| **Embedding Model** | Converting text to vectors | Finding relevant document sections |

**You need BOTH types for full functionality!**

---

## ⭐ Recommended LLM Models

### 🏆 Best for Thai Language

#### 1. Typhoon-v1.5x-7B (Thai Specialist)

**Why Choose This:**
- 🇹🇭 Developed by SCB 10X specifically for Thai
- 🎯 Best understanding of Thai context
- 📚 Handles Thai technical documents well

**How to Download:**
1. Open LM Studio
2. Click **Search** tab
3. Search: `typhoon-v1.5x-7b`
4. Look for **Typhoon-v1.5x-7b-Instruct**
5. Click **Download** (choose Q4_K_M version if available)
6. Wait for download (~4-5 GB)

**Requirements:**
- RAM: 8GB minimum
- Disk: ~5GB for model
- CPU: Works on modern CPUs

---

#### 2. Qwen2.5-7B-Instruct (All-Rounder)

**Why Choose This:**
- 🌍 Excellent multilingual support
- 🇹🇭 Good Thai + excellent English
- ⚡ Fast inference
- 📊 Great for technical documents

**How to Download:**
1. Open LM Studio
2. Click **Search** tab
3. Search: `qwen2.5-7b-instruct`
4. Click **Download** (Q4_K_M recommended)
5. Wait for download (~4-5 GB)

**Requirements:**
- RAM: 8GB minimum
- Disk: ~5GB for model

---

#### 3. Llama-3.1-8B-Instruct (Meta's Model)

**Why Choose This:**
- 🏢 From Meta (Facebook)
- 📈 Latest Llama version
- 🌐 Good multilingual
- ⚠️ Slightly larger, needs more RAM

**How to Download:**
1. Open LM Studio
2. Click **Search** tab
3. Search: `llama-3.1-8b-instruct`
4. Click **Download** (Q4_K_M recommended)
5. Wait for download (~5-6 GB)

**Requirements:**
- RAM: 10GB minimum
- Disk: ~6GB for model

---

### 📊 LLM Model Comparison

| Model | RAM | Disk | Thai | English | Speed |
|---|---|---|---|---|---|
| **Typhoon-v1.5x-7B** | 8GB | 5GB | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Qwen2.5-7B** | 8GB | 5GB | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Llama-3.1-8B** | 10GB | 6GB | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Mistral-7B** | 8GB | 5GB | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

---

## 🔤 Recommended Embedding Models

### 🏆 Best for Document Search

#### 1. bge-m3 (Recommended)

**Why Choose This:**
- 🌍 Supports 100+ languages including Thai
- 📊 High-quality embeddings
- 🎯 Best for mixed Thai-English documents

**How to Download:**
1. Open LM Studio
2. Click **Search** tab
3. Search: `bge-m3`
4. Click **Download**
5. Wait for download (~2GB)

---

#### 2. BAAI/bge-base-th (Thai Specialist)

**Why Choose This:**
- 🇹🇭 Specifically trained for Thai
- 📚 Better Thai semantic understanding
- ⚡ Smaller, faster

**How to Download:**
1. Open LM Studio
2. Click **Search** tab
3. Search: `bge-base-th`
4. Click **Download**
5. Wait for download (~500MB)

---

### 📊 Embedding Model Comparison

| Model | Size | Thai | English | Speed |
|---|---|---|---|---|
| **bge-m3** | ~2GB | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **bge-base-th** | ~500MB | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **multilingual-e5-large** | ~1.5GB | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

---

## 🖥️ Step 4: Start the Server

### Start API Server

1. Click the **Local Server** tab (server icon 🖥️)
2. Select your downloaded **LLM model** from dropdown
3. Configure settings:
   - **Context Length**: 4096 or higher
   - **GPU Offload**: Max (if you have GPU)
   - **Port**: 1234 (default)
4. Click **"Start Server"** button

### Verify Server is Running

- You should see a green indicator
- Server URL: `http://localhost:1234`
- Try visiting: http://localhost:1234/health

---

## 🎯 Step 5: Connect to PDF Summarizer

### Auto-Detection

The PDF Summarizer app will automatically detect LM Studio!

1. Start LM Studio server
2. Run PDF Summarizer (`start.bat` or `.exe`)
3. Check the status indicator (top-right)
4. Green dot = Connected! ✅

### Manual Configuration (if needed)

Create `.env` file:
```bash
LM_STUDIO_URL=http://localhost:1234
LLM_MODEL=qwen2.5-7b-instruct
EMBEDDING_MODEL=bge-m3
```

---

## 💡 Pro Tips

### Performance Optimization

**1. Use Q4_K_M Quantization**
- Best balance of quality and speed
- Uses ~50% less RAM than full model
- Minimal quality loss

**2. GPU Offloading**
- If you have NVIDIA GPU, enable GPU offload
- Significantly faster inference
- Set GPU layers to max in LM Studio

**3. Close Other Apps**
- Free up RAM before running
- Especially important for 8GB RAM systems

### Best Practices

**1. Model Selection**
- Use **Typhoon-v1.5x** for Thai-heavy documents
- Use **Qwen2.5** for mixed Thai-English
- Use **Llama-3.1** for English-heavy documents

**2. Document Upload**
- Large PDFs take longer to process
- First run caches embeddings (faster next time)
- Scan PDFs need OCR (slower)

**3. Summary Quality**
- If summary is poor, try a different model
- Typhoon usually gives best Thai summaries
- You can customize summary prompts in the app

---

## 🛠️ Troubleshooting

### LM Studio Won't Start Server

**Problem:** Server button greyed out or fails

**Solutions:**
1. Make sure a model is downloaded and selected
2. Check if port 1234 is available
3. Restart LM Studio
4. Try a different model

### PDF Summarizer Can't Connect

**Problem:** Status shows red dot or "not reachable"

**Solutions:**
1. Verify LM Studio is running
2. Check server is started (green indicator)
3. Try visiting http://localhost:1234/health
4. Check firewall isn't blocking
5. Make sure model name matches exactly

### Model Not Responding

**Problem:** Server running but no responses

**Solutions:**
1. Check model is fully downloaded
2. Try a simpler question first
3. Check RAM usage (model may have crashed)
4. Restart LM Studio and server
5. Try a different model

### Out of Memory

**Problem:** "Out of memory" or crashes

**Solutions:**
1. Use Q4_K_M quantization (smaller)
2. Close other applications
3. Use a smaller model (7B instead of 8B)
4. Reduce context length to 2048

---

## 📚 Additional Resources

### Official Documentation
- LM Studio: https://lmstudio.ai/docs
- FastAPI: https://fastapi.tiangolo.com/

### Model Downloads
- HuggingFace: https://huggingface.co
- Search for GGUF format models

### Community
- LM Studio Discord: https://discord.gg/lmstudio
- GitHub Issues: Report bugs here

---

## ✅ Quick Checklist

Before running PDF Summarizer:

- [ ] LM Studio installed and running
- [ ] LLM model downloaded (e.g., Qwen2.5-7B)
- [ ] Embedding model downloaded (e.g., bge-m3)
- [ ] Server started (green indicator)
- [ ] PDF Summarizer running
- [ ] Status shows green dot (connected)

If all checked ✅, you're ready to go!

---

**Need Help?** Open an issue on GitHub: https://github.com/ohm41321/Doc_Summary/issues
