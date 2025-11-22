# 🔧 SỬA LỖI DEPLOY

## ❌ Lỗi hiện tại:
```
ModuleNotFoundError: No module named 'app'
```

## ✅ Nguyên nhân:
Render đang chạy `gunicorn app:app` thay vì `gunicorn server:app`

## 🔧 Cách sửa:

### Bước 1: Kiểm tra Procfile
Đảm bảo Procfile có nội dung:
```
web: gunicorn server:app
```

### Bước 2: Sửa Start Command trên Render
1. Vào Render Dashboard
2. Chọn service `chatbot-bai-giang`
3. Vào tab **Settings**
4. Tìm phần **Start Command**
5. Sửa thành: `gunicorn server:app --bind 0.0.0.0:$PORT`
6. Click **Save Changes**

### Bước 3: Manual Deploy
1. Vào tab **Manual Deploy**
2. Click **Deploy latest commit**
3. Đợi deploy lại

---

## ✅ Hoặc sửa trực tiếp trên Render:

1. Vào **Settings** của service
2. Tìm **Start Command**
3. Đảm bảo là: `gunicorn server:app --bind 0.0.0.0:$PORT`
4. Save và Deploy lại

---

## 📝 Lưu ý:

- File Python của bạn là `server.py`
- App instance trong file là `app`
- Nên command phải là: `gunicorn server:app`

---

Sau khi sửa, deploy lại sẽ thành công! 🎉

