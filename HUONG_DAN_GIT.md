# 📦 HƯỚNG DẪN KHỞI TẠO GIT VÀ PUSH LÊN GITHUB

## ✅ Đã khởi tạo Git repository!

Bây giờ bạn cần:

---

## 📋 BƯỚC 1: TẠO REPOSITORY TRÊN GITHUB

1. Vào https://github.com → Đăng nhập
2. Click **New** (hoặc dấu + ở góc phải)
3. Điền thông tin:
   - **Repository name**: `chatbot-bai-giang`
   - **Description**: Chatbot Bài Giảng - Học từ tài liệu
   - **Visibility**: Public (hoặc Private)
4. **KHÔNG** tích "Initialize with README"
5. Click **Create repository**

---

## 📋 BƯỚC 2: COMMIT CODE

Chạy các lệnh sau trong terminal:

```bash
git commit -m "Initial commit - Chatbot Bài Giảng"
```

---

## 📋 BƯỚC 3: KẾT NỐI VỚI GITHUB

Sau khi tạo repository trên GitHub, bạn sẽ thấy URL. Chạy:

```bash
git remote add origin https://github.com/YOUR_USERNAME/chatbot-bai-giang.git
```

(Thay `YOUR_USERNAME` bằng username GitHub của bạn)

---

## 📋 BƯỚC 4: PUSH CODE LÊN GITHUB

```bash
git branch -M main
git push -u origin main
```

Nếu hỏi username/password:
- Username: Tên GitHub của bạn
- Password: Dùng **Personal Access Token** (không phải password thường)

### Tạo Personal Access Token:
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token
3. Chọn quyền: `repo`
4. Copy token và dùng làm password

---

## ✅ HOÀN TẤT!

Sau khi push thành công, code sẽ có trên GitHub và bạn có thể deploy!

---

## 🔍 KIỂM TRA

Vào https://github.com/YOUR_USERNAME/chatbot-bai-giang
- Nếu thấy tất cả files → Thành công! ✅

