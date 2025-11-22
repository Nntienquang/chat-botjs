# Chatbot Bài Giảng - Sử dụng Groq API (Llama 3.1)

Chatbot thông minh học từ tài liệu và trả lời câu hỏi sử dụng Groq API với Llama 3.1 (FREE, nhanh, mạnh).

## Tính năng

- ✅ Học từ tài liệu trong folder `doc/` (docx, pdf, txt)
- ✅ Sử dụng Groq API (Llama 3.1) để tạo câu trả lời thông minh
- ✅ Tìm kiếm semantic trong tài liệu
- ✅ Q&A dataset cho câu hỏi thường gặp
- ✅ Giao diện web đẹp, tích hợp PowerPoint
- ✅ **FREE** - Groq API miễn phí, nhanh, mạnh

## Cài đặt

```bash
pip install -r requirements.txt
```

## Chạy Local

```bash
python server.py
```

Hoặc dùng Anaconda:
```bash
conda activate your_env
python server.py
```

Sau đó mở trình duyệt: `http://localhost:5000`

## Deploy

### Render.com (Khuyến nghị - FREE)

1. Đăng ký/đăng nhập tại [render.com](https://render.com)
2. Tạo "New Web Service"
3. Kết nối GitHub repository
4. Cấu hình:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn server:app`
5. Deploy!

### Railway.app

1. Đăng ký tại [railway.app](https://railway.app)
2. Tạo project mới từ GitHub
3. Railway tự động detect và deploy

### Lưu ý

- Đảm bảo file `Procfile` có nội dung: `web: gunicorn server:app`
- File `runtime.txt` chỉ định Python version
- Groq API key đã được hardcode trong `chatbot.py` (có thể chuyển sang biến môi trường nếu cần)

## API

Sử dụng **Groq API** với model **Llama 3.1 8B Instant** - FREE, nhanh, mạnh, trả lời tự nhiên và chính xác.

