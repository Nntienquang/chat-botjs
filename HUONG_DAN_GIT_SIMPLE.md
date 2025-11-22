# 📦 HƯỚNG DẪN GIT - ĐƠN GIẢN

## ✅ Đã khởi tạo Git repository!

Bây giờ làm theo các bước sau:

---

## 📋 BƯỚC 1: CẤU HÌNH GIT (CHỈ LÀM 1 LẦN)

Chạy 2 lệnh sau (thay thông tin của bạn):

```bash
git config --global user.name "Tên của bạn"
git config --global user.email "email@example.com"
```

**Ví dụ:**
```bash
git config --global user.name "Nguyen Van A"
git config --global user.email "nguyenvana@gmail.com"
```

---

## 📋 BƯỚC 2: COMMIT CODE

```bash
git commit -m "Initial commit - Chatbot Bài Giảng"
```

---

## 📋 BƯỚC 3: TẠO REPOSITORY TRÊN GITHUB

1. Vào https://github.com → Đăng nhập
2. Click **New** (hoặc dấu +)
3. Điền:
   - **Repository name**: `chatbot-bai-giang`
   - **KHÔNG** tích "Initialize with README"
4. Click **Create repository**

---

## 📋 BƯỚC 4: KẾT NỐI VÀ PUSH

Sau khi tạo repository, GitHub sẽ hiển thị URL. Chạy:

```bash
git remote add origin https://github.com/YOUR_USERNAME/chatbot-bai-giang.git
git branch -M main
git push -u origin main
```

(Thay `YOUR_USERNAME` bằng username GitHub của bạn)

---

## 🔐 NẾU HỎI PASSWORD:

Dùng **Personal Access Token** (không phải password thường):

1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. **Generate new token (classic)**
3. Đặt tên: `chatbot-deploy`
4. Chọn quyền: ✅ **repo** (tất cả)
5. Click **Generate token**
6. **Copy token** (chỉ hiện 1 lần!)
7. Dùng token này làm password khi push

---

## ✅ HOÀN TẤT!

Sau khi push thành công:
- Code sẽ có trên GitHub
- Có thể deploy trên Render/Railway
- URL: `https://github.com/YOUR_USERNAME/chatbot-bai-giang`

---

## 🔍 KIỂM TRA

Vào repository trên GitHub, nếu thấy:
- ✅ `chatbot.py`
- ✅ `server.py`
- ✅ `requirements.txt`
- ✅ `Procfile`
- ✅ `qa_dataset.json`
- ✅ Folder `doc/`

→ **THÀNH CÔNG!** 🎉

