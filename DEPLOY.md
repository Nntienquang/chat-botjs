# Hướng Dẫn Deploy Chatbot

## Chuẩn Bị

1. Đảm bảo đã commit tất cả code lên GitHub
2. Có tài khoản trên platform deploy (Render/Railway)

## Deploy lên Render.com (FREE)

### Bước 1: Tạo Repository trên GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-github-repo-url>
git push -u origin main
```

### Bước 2: Deploy trên Render
1. Đăng nhập [render.com](https://render.com)
2. Click "New" → "Web Service"
3. Kết nối GitHub repository
4. Cấu hình:
   - **Name**: chatbot-bai-giang (hoặc tên bạn muốn)
   - **Region**: Singapore (gần Việt Nam nhất)
   - **Branch**: main
   - **Root Directory**: (để trống)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn server:app`
5. Click "Create Web Service"
6. Đợi deploy xong (5-10 phút)

### Bước 3: Lấy URL
Sau khi deploy xong, bạn sẽ có URL dạng: `https://chatbot-bai-giang.onrender.com`

## Deploy lên Railway.app

1. Đăng nhập [railway.app](https://railway.app)
2. Click "New Project" → "Deploy from GitHub repo"
3. Chọn repository
4. Railway tự động detect và deploy
5. Lấy URL từ dashboard

## Kiểm Tra

Sau khi deploy, truy cập URL và test chatbot:
- Giao diện web hiển thị đúng
- Chatbot trả lời được câu hỏi
- API hoạt động (check Usage trên Groq dashboard)

## Cấu Hình Biến Môi Trường

**QUAN TRỌNG**: Cần thêm Groq API Key vào biến môi trường:

### Lấy API Key:
1. Đăng nhập [Groq Console](https://console.groq.com/keys)
2. Tạo API key mới hoặc copy key hiện có

### Render.com:
1. Vào Settings → Environment
2. Add Environment Variable:
   - **Key**: `GROQ_API_KEY`
   - **Value**: `[Paste API key của bạn vào đây]`
3. Save Changes

### Railway.app:
1. Vào Variables tab
2. Add Variable:
   - **Key**: `GROQ_API_KEY`
   - **Value**: `[Paste API key của bạn vào đây]`
3. Deploy lại

## Lưu Ý

- Render.com FREE tier có thể sleep sau 15 phút không dùng
- Railway.app có free tier nhưng giới hạn
- Nếu cần 24/7, có thể upgrade hoặc dùng Cyclic.sh
- **KHÔNG** commit API key vào Git (đã được bảo vệ)

## Tích Hợp PowerPoint

Sau khi có URL, có thể tích hợp vào PowerPoint:
1. Insert → Web Page
2. Nhập URL của chatbot
3. Resize và điều chỉnh kích thước

