# 🚂 DEPLOY TRÊN RAILWAY - ĐƠN GIẢN NHẤT

## ✅ Ưu điểm Railway:
- Tự động detect Python
- Không cần Procfile (tự động)
- Deploy nhanh (3-5 phút)
- Free tier tốt
- Dễ sử dụng

---

## 📋 BƯỚC 1: CHUẨN BỊ GITHUB

1. Đảm bảo code đã upload lên GitHub
2. Repository có tất cả files:
   - `chatbot.py`
   - `server.py`
   - `requirements.txt`
   - `qa_dataset.json`
   - Folder `doc/`

---

## 📋 BƯỚC 2: DEPLOY TRÊN RAILWAY

### 2.1. Đăng ký
1. Vào https://railway.app
2. Click **Start a New Project**
3. Chọn **Sign up with GitHub**
4. Authorize Railway

### 2.2. Tạo Project
1. Click **New Project**
2. Chọn **Deploy from GitHub repo**
3. Chọn repository `chatbot-bai-giang`
4. Railway tự động detect Python và deploy!

### 2.3. Cấu hình (nếu cần)
1. Vào **Settings** của service
2. **Deploy** tab:
   - **Start Command**: `gunicorn server:app --bind 0.0.0.0:$PORT`
   - Railway tự động set PORT, nhưng có thể set thủ công

### 2.4. Đợi deploy
- Railway tự động:
  - Detect Python
  - Install dependencies
  - Deploy app
- Thời gian: 3-5 phút
- Xem progress trong **Deployments**

### 2.5. Lấy URL
1. Vào **Settings** → **Networking**
2. Click **Generate Domain**
3. URL sẽ là: `https://chatbot-bai-giang.up.railway.app`
4. Copy URL này!

---

## 📋 BƯỚC 3: TEST

1. Mở URL trong trình duyệt
2. Test: "Tên thật của Hàn Mặc Tử là gì?"
3. Nếu trả lời đúng → **THÀNH CÔNG!** 🎉

---

## ⚠️ LƯU Ý

### Free Tier:
- **$5 credit/tháng** (đủ dùng)
- **500 giờ runtime/tháng**
- **100GB bandwidth/tháng**

### Nếu hết credit:
- Railway sẽ pause service
- Có thể upgrade lên paid plan
- Hoặc chuyển sang nền tảng khác

---

## 🔧 TROUBLESHOOTING

### Lỗi: Service không start
- Kiểm tra **Start Command**: `gunicorn server:app --bind 0.0.0.0:$PORT`
- Xem **Logs** để biết lỗi cụ thể

### Lỗi: Module not found
- Kiểm tra `requirements.txt` đầy đủ
- Railway sẽ tự động install

### Lỗi: Port not found
- Railway tự động set PORT
- Đảm bảo code dùng `os.environ.get('PORT', 5000)`

---

## ✅ SO VỚI RENDER

| Tính năng | Railway | Render |
|-----------|---------|--------|
| Tự động detect | ✅ Có | ❌ Không |
| Cần Procfile | ❌ Không | ✅ Có |
| Free tier | ✅ $5/tháng | ✅ Free |
| Sleep | ❌ Không | ✅ Có (15 phút) |
| Tốc độ | ⚡ Nhanh | ⚡ Nhanh |

---

**Railway dễ hơn Render vì tự động detect mọi thứ! 🚀**

