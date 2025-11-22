# 🚀 DEPLOY ĐƠN GIẢN - 3 BƯỚC

## BƯỚC 1: Upload lên GitHub (5 phút)

### 1.1. Tạo repository
1. Vào https://github.com → Đăng nhập
2. Click **New** (hoặc dấu +)
3. Điền:
   - **Repository name**: `chatbot-bai-giang`
   - Click **Create repository**

### 1.2. Upload files
**Cách dễ nhất:**
1. Vào repository vừa tạo
2. Click **Add file** → **Upload files**
3. Kéo thả TẤT CẢ files từ folder `D:\chatbot` vào:
   - `chatbot.py`
   - `server.py`
   - `requirements.txt`
   - `Procfile`
   - `runtime.txt`
   - `qa_dataset.json`
   - Folder `doc/` (kéo cả folder)
4. Click **Commit changes**

---

## BƯỚC 2: Deploy trên Render (5 phút)

### 2.1. Đăng ký
1. Vào https://render.com
2. Click **Get Started for Free**
3. Chọn **Sign up with GitHub**
4. Authorize Render

### 2.2. Tạo Web Service
1. Dashboard → **New +** → **Web Service**
2. **Connect repository**: Chọn `chatbot-bai-giang`
3. Điền:
   ```
   Name: chatbot-bai-giang
   Region: Singapore
   Branch: main
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn server:app --bind 0.0.0.0:$PORT
   
   ⚠️ QUAN TRỌNG: Phải là `server:app` (không phải `app:app`)!
   Plan: Free
   ```
4. Click **Create Web Service**

### 2.3. Đợi deploy
- Đợi 5-10 phút
- Xem progress trong tab **Logs**
- Khi thấy "Your service is live" → Thành công!

### 2.4. Copy URL
- URL sẽ là: `https://chatbot-bai-giang.onrender.com`
- Copy URL này!

---

## BƯỚC 3: Tích hợp PowerPoint (2 phút)

### Cách 1: Web Viewer
1. Mở PowerPoint
2. **Insert** → **Get Add-ins** → Tìm "Web Viewer"
3. Nhập URL chatbot
4. Resize cho đẹp
5. Xong!

### Cách 2: Hyperlink
1. Tạo button/text
2. Right-click → **Hyperlink**
3. Nhập URL chatbot
4. Xong!

---

## ✅ TEST

1. Mở URL trong trình duyệt
2. Hỏi: "Tên thật của Hàn Mặc Tử là gì?"
3. Nếu trả lời đúng → **THÀNH CÔNG!** 🎉

---

## ⚠️ LƯU Ý

- **Free tier**: Sleep sau 15 phút không dùng (wake up mất ~30s)
- **Lần đầu**: Có thể chậm (download models)
- **Tài liệu**: Đảm bảo folder `doc/` đã upload

---

## 🆘 GẶP LỖI?

1. Kiểm tra **Logs** trên Render
2. Đảm bảo tất cả files đã upload
3. Kiểm tra `requirements.txt` có `gunicorn`

---

**Chúc bạn thành công! 🚀**

