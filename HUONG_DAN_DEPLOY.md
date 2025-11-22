# HƯỚNG DẪN DEPLOY CHATBOT BÀI GIẢNG

## 🚀 Các nền tảng deploy miễn phí

### Option 1: Render.com (Khuyến nghị - Dễ nhất)

#### Bước 1: Chuẩn bị
1. Tạo tài khoản tại https://render.com (miễn phí)
2. Kết nối với GitHub/GitLab/Bitbucket

#### Bước 2: Deploy
1. Vào Dashboard → New → Web Service
2. Kết nối repository của bạn
3. Cấu hình:
   - **Name**: chatbot-bai-giang
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn server:app --bind 0.0.0.0:$PORT`
   - **Plan**: Free

4. Thêm Environment Variables (nếu cần):
   - `PORT`: 10000 (Render tự động set)

5. Click "Create Web Service"

#### Bước 3: Lấy URL
- Sau khi deploy xong, bạn sẽ có URL dạng: `https://chatbot-bai-giang.onrender.com`
- URL này công khai, ai cũng có thể truy cập!

---

### Option 2: Railway.app

#### Bước 1: Chuẩn bị
1. Tạo tài khoản tại https://railway.app
2. Cài đặt Railway CLI (tùy chọn)

#### Bước 2: Deploy
1. Vào Dashboard → New Project → Deploy from GitHub
2. Chọn repository
3. Railway tự động detect Python và deploy
4. Thêm biến môi trường `PORT` (Railway tự động set)

#### Bước 3: Lấy URL
- Railway tự động tạo URL: `https://your-app.up.railway.app`

---

### Option 3: PythonAnywhere

#### Bước 1: Đăng ký
1. Tạo tài khoản miễn phí tại https://www.pythonanywhere.com

#### Bước 2: Upload code
1. Vào Files tab
2. Upload tất cả files (chatbot.py, server.py, requirements.txt, qa_dataset.json, folder doc/)
3. Tạo thư mục `mysite/` trong home directory

#### Bước 3: Cấu hình
1. Vào Web tab → Add a new web app
2. Chọn Flask, Python 3.10
3. Cấu hình WSGI file:
```python
import sys
path = '/home/yourusername/mysite'
if path not in sys.path:
    sys.path.append(path)

from server import app as application
```

4. Reload web app

#### Bước 4: Lấy URL
- URL: `https://yourusername.pythonanywhere.com`

---

### Option 4: Heroku (Có thể mất phí)

#### Bước 1: Cài đặt Heroku CLI
```bash
# Windows: Download từ https://devcenter.heroku.com/articles/heroku-cli
```

#### Bước 2: Login và deploy
```bash
heroku login
heroku create chatbot-bai-giang
git init
git add .
git commit -m "Initial commit"
git push heroku main
```

---

## 📋 Checklist trước khi deploy

- [ ] File `requirements.txt` đã có đầy đủ dependencies
- [ ] File `Procfile` đã tạo (cho Render/Heroku)
- [ ] File `runtime.txt` đã tạo (cho Render)
- [ ] Folder `doc/` có tài liệu
- [ ] File `qa_dataset.json` đã có
- [ ] Test local trước khi deploy

---

## 🔧 Cấu hình server.py cho production

File `server.py` đã được cấu hình sẵn với:
- `host='0.0.0.0'` - Cho phép truy cập từ bên ngoài
- `port=5000` hoặc `$PORT` - Tự động lấy port từ environment

---

## 🎯 Tích hợp vào PowerPoint

Sau khi deploy, bạn có URL công khai (ví dụ: `https://chatbot-bai-giang.onrender.com`)

### Cách 1: Embed iframe (Khuyến nghị)

1. Mở PowerPoint
2. Insert → Get Add-ins → Web Viewer (hoặc Online Video)
3. Nhập URL: `https://chatbot-bai-giang.onrender.com`
4. Resize và đặt vị trí
5. Khi trình chiếu, click vào slide để mở chatbot

### Cách 2: Hyperlink

1. Tạo một shape hoặc text
2. Right-click → Hyperlink
3. Nhập URL: `https://chatbot-bai-giang.onrender.com`
4. Khi click sẽ mở chatbot trong trình duyệt

### Cách 3: Action Button

1. Insert → Shapes → Action Buttons
2. Chọn button
3. Hyperlink to → URL
4. Nhập URL: `https://chatbot-bai-giang.onrender.com`

---

## 🌐 Lưu ý quan trọng

1. **Free tier có giới hạn**:
   - Render: Sleep sau 15 phút không dùng (wake up mất ~30s)
   - Railway: Có giới hạn usage
   - PythonAnywhere: Chỉ chạy khi có người truy cập

2. **Tài liệu**:
   - Đảm bảo folder `doc/` được upload đầy đủ
   - File `qa_dataset.json` phải có trong root

3. **Performance**:
   - Lần đầu load có thể chậm (download models)
   - Các lần sau sẽ nhanh hơn

4. **Security**:
   - URL công khai, ai cũng có thể dùng
   - Không lưu thông tin nhạy cảm

---

## ✅ Test sau khi deploy

1. Mở URL trong trình duyệt
2. Test các câu hỏi:
   - "Tên thật của Hàn Mặc Tử là gì?"
   - "Khổ 4"
   - "Tóm tắt nội dung"
3. Kiểm tra tích hợp vào PowerPoint

---

## 🆘 Troubleshooting

### Lỗi: Module not found
- Kiểm tra `requirements.txt` đã có đầy đủ
- Rebuild application

### Lỗi: Port already in use
- Đảm bảo dùng `$PORT` environment variable
- Render/Railway tự động set PORT

### Lỗi: Cannot find doc folder
- Đảm bảo upload folder `doc/` lên server
- Kiểm tra đường dẫn trong code

### Chatbot không trả lời đúng
- Kiểm tra `qa_dataset.json` đã upload
- Kiểm tra folder `doc/` có tài liệu
- Xem logs trên platform để debug

---

## 📞 Hỗ trợ

Nếu gặp vấn đề, kiểm tra:
1. Logs trên platform (Render/Railway có logs tab)
2. Test local trước
3. Kiểm tra file cấu hình

