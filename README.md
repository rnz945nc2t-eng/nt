# 🚀 Gemini Deep Research Engine - Complete Solution

## 📦 Package Contents

This package contains **3 different solutions** to fix the CORS/"Failed to fetch" error:

### 1️⃣ **Frontend-Only (CORS Proxy)**
- **File**: `gemini-nexus-cors-fixed.html`
- Uses public CORS proxies
- No backend needed
- May have reliability issues

### 2️⃣ **Backend Solution** (⭐ RECOMMENDED)
- **Files**: `backend_server.py`, `frontend_backend.html`, `requirements.txt`
- Python Flask server handles API calls
- 100% reliable, no CORS issues
- Best for production use

### 3️⃣ **Original Version**
- **File**: `gemini-deepsearch-evolved.html`
- Direct API calls (may fail due to CORS)
- Reference implementation

---

## 🎯 Recommended: Backend Solution Setup

This is the **most reliable** way to run the engine.

### Step 1: Install Python Dependencies

```bash
# Install required packages
pip install -r requirements.txt
```

Or install manually:
```bash
pip install Flask==3.0.0 flask-cors==4.0.0 requests==2.31.0
```

### Step 2: Start the Backend Server

```bash
python backend_server.py
```

You should see:
```
============================================================
🚀 GEMINI RESEARCH BACKEND SERVER
============================================================
Server starting on http://localhost:5000

Available endpoints:
  POST /api/gemini - Call Gemini API
  GET  /api/wikipedia?q=query - Fetch Wikipedia
  GET  /api/duckduckgo?q=query - Fetch DuckDuckGo

Press Ctrl+C to stop
============================================================
 * Running on http://0.0.0.0:5000
```

### Step 3: Open the Frontend

1. Open `frontend_backend.html` in your browser
2. You should see "Backend Online" status (green)
3. Enter your research query and click "RESEARCH"

---

## 🔧 Alternative: CORS Proxy Version

If you can't run a Python backend, try this:

### Option A: Browser Extension
1. Install a CORS extension:
   - Chrome: "CORS Unblock" or "Allow CORS"
   - Firefox: "CORS Everywhere"
2. Enable the extension
3. Open `gemini-nexus-cors-fixed.html`

### Option B: Local Server
```bash
# Python 3
python -m http.server 8000

# Then open: http://localhost:8000/gemini-nexus-cors-fixed.html
```

---

## 🔑 API Keys Setup

You need **2 Gemini API keys** for dual-engine mode:

1. Go to: https://makersuite.google.com/app/apikey
2. Create 2 API keys (or use the same key twice)
3. Paste them into the "Primary Engine Key" and "Refinement Engine Key" fields

---

## ❓ Troubleshooting

### "Backend Offline" Error
**Problem**: Frontend can't connect to backend server

**Solutions**:
1. Make sure `backend_server.py` is running
2. Check that you're using the correct URL (`http://localhost:5000`)
3. Check firewall settings

### "Failed to fetch" Error (Frontend-only versions)
**Problem**: Browser blocking CORS

**Solutions**:
1. ✅ **Best**: Use the backend solution
2. Install a CORS browser extension
3. Run from localhost server
4. Try a different browser

### "Quota Exceeded" Error
**Problem**: API rate limits hit

**Solutions**:
1. Wait 60 seconds
2. Use different API keys
3. The dual-key system helps prevent this

### "Invalid API Key" Error
**Problem**: Wrong or expired keys

**Solutions**:
1. Generate new keys at https://makersuite.google.com/app/apikey
2. Make sure you copied the full key
3. Check for extra spaces

---

## 🎨 Features

✅ **Dual-Engine Architecture** - Two-pass research for higher quality
✅ **Multi-Source Synthesis** - Wikipedia + DuckDuckGo + Gemini knowledge
✅ **Automatic Model Fallback** - Tries multiple Gemini models
✅ **Real-time Progress** - Visual feedback for each phase
✅ **Professional UI** - Cyberpunk-inspired design
✅ **Error Recovery** - Robust error handling

---

## 📊 How It Works

```
1. DATA GATHERING
   ├─ Fetch Wikipedia articles
   ├─ Fetch DuckDuckGo summary
   └─ Aggregate sources

2. PRIMARY SYNTHESIS (Engine 1 / Key 1)
   ├─ Combine external data
   ├─ Apply AI knowledge
   └─ Generate comprehensive draft

3. COOLING PERIOD (3 seconds)
   └─ Prevent rate limiting

4. REFINEMENT PASS (Engine 2 / Key 2)
   ├─ Critical analysis
   ├─ Polish language
   ├─ Add synthesis verdict
   └─ Final quality check

5. RENDER RESULTS
   └─ Display formatted report
```

---

## 🚨 Important Notes

⚠️ **API Keys**: Never share your API keys publicly or commit them to Git

⚠️ **Rate Limits**: Gemini has rate limits (15 requests/minute on free tier)

⚠️ **CORS**: Direct browser-to-API calls are blocked by most browsers for security

⚠️ **Data Sources**: Wikipedia and DuckDuckGo may occasionally be unavailable

---

## 📝 File Descriptions

| File | Purpose |
|------|---------|
| `backend_server.py` | Python Flask server (bypasses CORS) |
| `frontend_backend.html` | Frontend for backend version |
| `gemini-nexus-cors-fixed.html` | Frontend-only with CORS workarounds |
| `gemini-deepsearch-evolved.html` | Original direct API version |
| `requirements.txt` | Python dependencies |
| `README.md` | This file |

---

## 🎯 Quick Start (TL;DR)

```bash
# 1. Install dependencies
pip install Flask flask-cors requests

# 2. Start backend
python backend_server.py

# 3. Open in browser
open frontend_backend.html

# 4. Add your API keys and start researching!
```

---

## 💡 Tips for Best Results

1. **Use specific queries**: "Impact of AI on healthcare 2024" vs "AI healthcare"
2. **Let it complete**: Both passes take 30-60 seconds total
3. **Review synthesis verdict**: Key takeaways at the end
4. **Save your keys**: Browser remembers them between sessions

---

## 🆘 Still Having Issues?

1. Check the browser console (F12) for detailed errors
2. Verify backend is running: http://localhost:5000
3. Test API keys directly at: https://makersuite.google.com
4. Try the CORS proxy version as fallback

---

## ⚡ Made with Claude

This engine was created and evolved by Claude to provide a robust, production-ready research tool with multiple deployment options.

**Version**: 3.0 (Backend Edition)
**Last Updated**: February 2026
