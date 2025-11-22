# 🚀 DEPLOY NHANH - 5 PHÚT

## Render.com (Khuyến nghị - Dễ nhất)

### Bước 1: Chuẩn bị GitHub
1. Tạo repository mới trên GitHub
2. Upload tất cả files:
   - chatbot.py
   - server.py
   - requirements.txt
   - Procfile
   - runtime.txt
   - qa_dataset.json
   - folder doc/ (với tài liệu bên trong)

### Bước 2: Deploy trên Render
1. Vào https://render.com → Sign up (dùng GitHub)
2. New → Web Service
3. Connect repository của bạn
4. Điền thông tin:
   - **Name**: chatbot-bai-giang
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn server:app --bind 0.0.0.0:$PORT` ⚠️ QUAN TRỌNG: Phải là `server:app` không phải `app:app`!
5. Click "Create Web Service"
6. Đợi 5-10 phút để deploy xong

### Bước 3: Lấy URL
- Sau khi deploy xong, copy URL (ví dụ: `https://chatbot-bai-giang.onrender.com`)
- URL này công khai, ai cũng dùng được!

---

## 🎯 Tích hợp vào PowerPoint

### Cách đơn giản nhất:

1. **Mở PowerPoint**
2. **Insert → Get Add-ins → Web Viewer**
3. **Nhập URL** bạn vừa copy
4. **Resize** cho vừa slide
5. **Xong!** Khi trình chiếu, click vào để mở chatbot

### Hoặc dùng Hyperlink:

1. Tạo một button hoặc text
2. Right-click → **Hyperlink**
3. Nhập URL chatbot
4. Khi click sẽ mở chatbot trong trình duyệt

---

## ✅ Test

1. Mở URL trong trình duyệt
2. Test: "Tên thật của Hàn Mặc Tử là gì?"
3. Nếu trả lời đúng → Thành công!

---

## ⚠️ Lưu ý

- **Free tier**: Render sẽ sleep sau 15 phút không dùng
- **Lần đầu**: Có thể chậm (download models)
- **Tài liệu**: Đảm bảo folder `doc/` đã upload đầy đủ

---

## 🆘 Gặp lỗi?

1. Kiểm tra logs trên Render (tab Logs)
2. Đảm bảo tất cả files đã upload
3. Kiểm tra `requirements.txt` đầy đủ

