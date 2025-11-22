# ✅ CHECKLIST DEPLOY TRÊN RENDER

## 📋 CẤU HÌNH TRÊN RENDER

### 1. Service Name
- ✅ `chat-botjs-4` (hoặc tên bạn muốn)

### 2. Language
- ✅ `Python 3`

### 3. Branch
- ✅ `main`

### 4. Region
- ✅ `Oregon (US West)` hoặc `Singapore` (gần VN hơn)

### 5. Root Directory
- ✅ Để trống (hoặc không điền gì)

### 6. Build Command
- ✅ `pip install -r requirements.txt`

### 7. Start Command ⚠️ QUAN TRỌNG!
- ✅ `gunicorn server:app --timeout 120`
- ❌ KHÔNG dùng `gunicorn app:app` (sai!)

### 8. Instance Type
- ✅ `Free` ($0/month) - đủ dùng với phiên bản deploy nhẹ

### 9. Environment Variables
- ✅ `GROQ_API_KEY` = `[Paste API key của bạn vào đây]`

## 📁 FILES CẦN CÓ TRONG REPO

- ✅ `server.py` - Web server
- ✅ `chatbot_deploy.py` - Chatbot phiên bản deploy
- ✅ `chatbot.py` - Chatbot phiên bản local (backup)
- ✅ `embeddings.npy` - Embeddings đã tính sẵn
- ✅ `chunks.json` - Chunks text
- ✅ `qa_dataset.json` - Q&A dataset
- ✅ `requirements.txt` - Dependencies
- ✅ `Procfile` - Start command
- ✅ `runtime.txt` - Python version
- ✅ `doc/Mua_Xuan_Chin.docx` - Tài liệu (không dùng trên deploy)

## 🚀 SAU KHI DEPLOY

1. Đợi build xong (5-10 phút)
2. Kiểm tra logs:
   - Tìm: `🚀 DEPLOY MODE: Sử dụng chatbot_deploy`
   - Tìm: `✅ Loaded X chunks & embeddings`
   - Tìm: `✅ Chatbot đã sẵn sàng!`
3. Test: `https://your-service.onrender.com/health`
4. Test chatbot: `https://your-service.onrender.com`

## ⚠️ LƯU Ý

- **Start Command PHẢI là**: `gunicorn server:app --timeout 120`
- Nếu thiếu `embeddings.npy` hoặc `chunks.json`, deploy sẽ FAIL!
- Free tier có thể sleep sau 15 phút không dùng (wake up mất ~50s)

