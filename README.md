# Chatbot Tài Liệu - Tích Hợp PowerPoint

Chatbot đọc và học từ tài liệu trong folder `doc`, sau đó trả lời câu hỏi qua giao diện web HTML để tích hợp vào PowerPoint.

## 🚀 Cách Chạy

### Bước 1: Cài đặt thư viện (chỉ làm 1 lần)

Mở **Anaconda Prompt** và chạy:
```bash
cd D:\chatbot
pip install -r requirements.txt
```

### Bước 2: Chạy Web Server

**Double-click file `CHAY.bat`**

Hoặc mở Anaconda Prompt:
```bash
cd D:\chatbot
python server.py
```

Server sẽ chạy tại: **http://localhost:5000**

## 📊 Tích Hợp Vào PowerPoint

**Xem hướng dẫn chi tiết trong file `HUONG_DAN_POWERPOINT.md`**

### Cách nhanh:

1. **Chạy server**: Double-click `CHAY.bat`
2. **Mở PowerPoint** → Vào slide cần thêm chatbot
3. **Insert** → **Get Add-ins** → Tìm "**Web Viewer**"
4. Nhập URL: `http://localhost:5000`
5. Click **Insert** → Xong!

**Lưu ý**: Phải giữ server chạy trong khi trình bày PowerPoint!

## 📁 Cấu trúc

```
chatbot/
├── doc/              # Đặt tài liệu vào đây (.docx, .pdf, .txt)
├── chatbot.py        # Logic chatbot
├── server.py         # Web server
├── CHAY.bat          # Chạy server (double-click)
├── requirements.txt  # Thư viện cần thiết
└── README.md         # File này
```

## ⚠️ Lưu ý

- **Phải chạy server** trước khi trình bày PowerPoint
- Server chạy tại `http://localhost:5000`
- Lần đầu chạy sẽ tải mô hình AI (cần internet, mất 5-10 phút)
- Đảm bảo có tài liệu trong folder `doc/`

## 💡 Tip

Khi trình bày, để chatbot luôn sẵn sàng:
1. Chạy server trước khi mở PowerPoint
2. Giữ cửa sổ server mở trong khi trình bày
3. Chatbot sẽ hoạt động trong slide PowerPoint

