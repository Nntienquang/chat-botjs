# 🚀 HƯỚNG DẪN DEPLOY TỪNG BƯỚC - CHI TIẾT

## 📋 BƯỚC 1: CHUẨN BỊ GITHUB

### 1.1. Tạo tài khoản GitHub (nếu chưa có)
- Vào https://github.com → Sign up
- Xác thực email

### 1.2. Tạo repository mới
1. Vào https://github.com/new
2. Điền thông tin:
   - **Repository name**: `chatbot-bai-giang`
   - **Description**: Chatbot Bài Giảng - Học từ tài liệu
   - **Visibility**: Public (hoặc Private)
3. Click **Create repository**

### 1.3. Upload files lên GitHub

**Cách 1: Dùng GitHub Desktop (Dễ nhất)**
1. Download GitHub Desktop: https://desktop.github.com
2. Cài đặt và đăng nhập
3. File → Clone repository → Chọn repository vừa tạo
4. Copy tất cả files vào folder repository
5. Commit & Push

**Cách 2: Dùng Git Command Line**
```bash
cd D:\chatbot
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/chatbot-bai-giang.git
git push -u origin main
```

**Cách 3: Upload trực tiếp trên web**
1. Vào repository trên GitHub
2. Click **Add file** → **Upload files**
3. Kéo thả tất cả files vào
4. Click **Commit changes**

### 📁 Files cần upload:
- ✅ `chatbot.py`
- ✅ `server.py`
- ✅ `requirements.txt`
- ✅ `Procfile`
- ✅ `runtime.txt`
- ✅ `qa_dataset.json`
- ✅ Folder `doc/` (với tài liệu bên trong)
- ✅ `.gitignore` (nếu có)

---

## 📋 BƯỚC 2: DEPLOY TRÊN RENDER.COM

### 2.1. Đăng ký tài khoản
1. Vào https://render.com
2. Click **Get Started for Free**
3. Chọn **Sign up with GitHub** (khuyến nghị)
4. Authorize Render để truy cập GitHub

### 2.2. Tạo Web Service
1. Vào Dashboard → Click **New +** → Chọn **Web Service**
2. **Connect repository**: Chọn repository `chatbot-bai-giang`
3. Điền thông tin:
   - **Name**: `chatbot-bai-giang`
   - **Region**: Singapore (gần Việt Nam nhất)
   - **Branch**: `main`
   - **Root Directory**: (để trống)
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn server:app --bind 0.0.0.0:$PORT`
   - **Plan**: Free

4. Click **Create Web Service**

### 2.3. Đợi deploy
- Render sẽ tự động build và deploy
- Thời gian: 5-10 phút
- Xem progress trong tab **Logs**

### 2.4. Lấy URL
- Sau khi deploy xong, bạn sẽ có URL: `https://chatbot-bai-giang.onrender.com`
- URL này công khai, ai cũng có thể truy cập!

---

## 📋 BƯỚC 3: KIỂM TRA VÀ TEST

### 3.1. Test URL
1. Mở trình duyệt
2. Vào URL vừa nhận được
3. Test các câu hỏi:
   - "Tên thật của Hàn Mặc Tử là gì?"
   - "Năm sinh của Hàn Mặc Tử?"
   - "Khổ 4"

### 3.2. Kiểm tra logs (nếu có lỗi)
1. Vào Render Dashboard
2. Chọn service → Tab **Logs**
3. Xem lỗi (nếu có) và sửa

---

## 📋 BƯỚC 4: TÍCH HỢP VÀO POWERPOINT

### 4.1. Cách 1: Web Viewer (Khuyến nghị)
1. Mở PowerPoint
2. **Insert** → **Get Add-ins**
3. Tìm "**Web Viewer**" → **Add**
4. Nhập URL chatbot: `https://chatbot-bai-giang.onrender.com`
5. Resize và đặt vị trí
6. Xong!

### 4.2. Cách 2: Hyperlink
1. Tạo button hoặc text
2. Right-click → **Hyperlink**
3. Nhập URL chatbot
4. Khi click sẽ mở chatbot

---

## ⚠️ LƯU Ý QUAN TRỌNG

### Free Tier Limitations:
1. **Sleep sau 15 phút**: Nếu không có người dùng, service sẽ sleep
   - Lần đầu truy cập sau khi sleep: mất ~30 giây để wake up
   - Giải pháp: Dùng paid plan hoặc chấp nhận delay

2. **Giới hạn tài nguyên**: 
   - RAM: 512MB
   - CPU: Shared
   - Bandwidth: 100GB/tháng

3. **Build time**: 
   - Lần đầu build có thể lâu (download models)
   - Các lần sau nhanh hơn

### Troubleshooting:

**Lỗi: Build failed**
- Kiểm tra `requirements.txt` đầy đủ
- Kiểm tra `Procfile` đúng format
- Xem logs để biết lỗi cụ thể

**Lỗi: Module not found**
- Đảm bảo tất cả dependencies trong `requirements.txt`
- Rebuild service

**Lỗi: Port already in use**
- Đảm bảo dùng `$PORT` trong start command
- Render tự động set PORT

**Chatbot không trả lời**
- Kiểm tra folder `doc/` đã upload
- Kiểm tra `qa_dataset.json` đã upload
- Xem logs để debug

---

## 🎯 TÓM TẮT NHANH

1. ✅ Upload code lên GitHub
2. ✅ Đăng ký Render.com
3. ✅ Tạo Web Service → Connect GitHub
4. ✅ Đợi deploy xong
5. ✅ Copy URL và tích hợp vào PowerPoint
6. ✅ Xong!

---

## 📞 HỖ TRỢ

Nếu gặp vấn đề:
1. Kiểm tra logs trên Render
2. Đảm bảo tất cả files đã upload
3. Kiểm tra `requirements.txt` đầy đủ
4. Test local trước khi deploy

**Chúc bạn deploy thành công! 🎉**

