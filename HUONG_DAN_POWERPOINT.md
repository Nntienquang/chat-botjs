# Hướng Dẫn Tích Hợp Chatbot Vào PowerPoint Slide

## ✅ Chatbot đã chạy thành công!

Bạn đang thấy chatbot tại: `http://192.168.31.81:5000` hoặc `http://localhost:5000`

## 📊 Cách Tích Hợp Vào PowerPoint

### Cách 1: Sử dụng Web Viewer Add-in (Khuyến nghị)

1. **Mở PowerPoint**
2. **Vào slide** bạn muốn thêm chatbot
3. **Insert** → **Get Add-ins** (hoặc **My Add-ins**)
4. Tìm và cài đặt **"Web Viewer"** (nếu chưa có)
5. Nhập URL:
   - `http://localhost:5000` (nếu chạy trên cùng máy)
   - `http://192.168.31.81:5000` (nếu truy cập từ máy khác trong mạng)
6. Click **Insert**
7. Chatbot sẽ hiển thị trong slide!

### Cách 2: Sử dụng Hyperlink

1. **Tạo một shape hoặc text box** trên slide
2. Gõ text: "Mở Chatbot" hoặc "Hỏi Chatbot"
3. **Right-click** → **Hyperlink**
4. Nhập URL: `http://localhost:5000`
5. Khi trình bày, click vào link để mở chatbot trong trình duyệt

### Cách 3: Sử dụng Online Video (Workaround)

1. **Insert** → **Online Video**
2. Nhập URL: `http://localhost:5000`
3. PowerPoint sẽ nhúng trang web như video

## ⚠️ Lưu Ý Quan Trọng

### Khi Trình Bày:

1. **Phải chạy server trước** khi mở PowerPoint
   - Double-click `CHAY.bat`
   - Hoặc chạy: `python server.py` trong Anaconda Prompt

2. **Giữ server chạy** trong khi trình bày
   - Đừng đóng cửa sổ server
   - Server phải chạy để chatbot hoạt động

3. **URL để sử dụng:**
   - Trên cùng máy: `http://localhost:5000`
   - Từ máy khác: `http://192.168.31.81:5000` (IP của máy chạy server)

### Kiểm Tra:

- Mở trình duyệt và truy cập `http://localhost:5000`
- Nếu thấy chatbot = server đang chạy OK
- Nếu lỗi 404 = server chưa chạy hoặc đã tắt

## 🎯 Tối Ưu Cho Trình Bày

### Trước Khi Trình Bày:

1. ✅ Chạy server (double-click `CHAY.bat`)
2. ✅ Test chatbot trong trình duyệt
3. ✅ Mở PowerPoint và tích hợp chatbot vào slide
4. ✅ Test lại trong chế độ Slide Show

### Trong Khi Trình Bày:

- Server phải luôn chạy
- Có thể minimize cửa sổ server
- Chatbot sẽ hoạt động bình thường trong slide

## 💡 Tips

- **Fullscreen chatbot**: Trong PowerPoint, có thể phóng to Web Viewer để chatbot chiếm toàn bộ slide
- **Nhiều slide**: Có thể thêm chatbot vào nhiều slide khác nhau
- **Tắt server**: Nhấn Ctrl+C trong cửa sổ server khi không dùng nữa

## ❓ Gặp Vấn Đề?

**Chatbot không hiển thị trong PowerPoint:**
- Kiểm tra server có đang chạy không
- Thử mở URL trong trình duyệt trước
- Đảm bảo URL đúng: `http://localhost:5000`

**Chatbot không trả lời:**
- Kiểm tra có tài liệu trong folder `doc/` không
- Xem cửa sổ server có báo lỗi không
- Thử refresh trang trong PowerPoint

