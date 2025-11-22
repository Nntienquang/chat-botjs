# 🎯 HƯỚNG DẪN TÍCH HỢP VÀO POWERPOINT

Sau khi deploy chatbot lên server (có URL công khai), bạn có thể tích hợp vào PowerPoint theo các cách sau:

---

## 📌 CÁCH 1: Web Viewer (Khuyến nghị - Đẹp nhất)

### Bước 1: Cài Add-in
1. Mở PowerPoint
2. **Insert** → **Get Add-ins**
3. Tìm "**Web Viewer**" hoặc "**Online Video**"
4. Click **Add** để cài đặt

### Bước 2: Chèn Chatbot
1. Vào slide muốn chèn chatbot
2. **Insert** → **Web Viewer** (hoặc **Online Video**)
3. Nhập URL chatbot của bạn (ví dụ: `https://chatbot-bai-giang.onrender.com`)
4. Click **Insert**
5. Resize và đặt vị trí cho đẹp

### Bước 3: Trình chiếu
- Khi trình chiếu, click vào vùng chatbot
- Chatbot sẽ mở trong slide, học sinh có thể tương tác trực tiếp!

---

## 📌 CÁCH 2: Hyperlink (Đơn giản nhất)

### Bước 1: Tạo Button
1. **Insert** → **Shapes** → Chọn shape (ví dụ: Rounded Rectangle)
2. Vẽ button trên slide
3. Thêm text: "Hỏi Chatbot" hoặc "💬 Chatbot"

### Bước 2: Tạo Hyperlink
1. Right-click vào button
2. Chọn **Hyperlink**
3. Chọn **Existing File or Web Page**
4. Nhập URL chatbot vào ô **Address**
5. Click **OK**

### Bước 3: Trình chiếu
- Khi click button, chatbot sẽ mở trong trình duyệt mặc định
- Học sinh có thể tương tác với chatbot

---

## 📌 CÁCH 3: Action Button (Chuyên nghiệp)

### Bước 1: Tạo Action Button
1. **Insert** → **Shapes** → **Action Buttons**
2. Chọn button style (ví dụ: Information)
3. Vẽ button trên slide

### Bước 2: Cấu hình
1. Hộp thoại **Action Settings** tự động mở
2. Chọn **Hyperlink to** → **URL...**
3. Nhập URL chatbot
4. Click **OK**

### Bước 3: Trình chiếu
- Click button để mở chatbot

---

## 📌 CÁCH 4: Embed HTML (Nâng cao)

### Bước 1: Tạo HTML file
Tạo file `chatbot.html` với nội dung:
```html
<iframe src="https://chatbot-bai-giang.onrender.com" 
        width="100%" 
        height="600px" 
        frameborder="0">
</iframe>
```

### Bước 2: Chèn vào PowerPoint
1. **Insert** → **Object**
2. Chọn **Create from file**
3. Chọn file HTML
4. Click **OK**

---

## 🎨 TIPS - Làm đẹp hơn

### 1. Tạo Background đẹp
- Thêm background gradient hoặc hình ảnh
- Đảm bảo chatbot nổi bật

### 2. Thêm Icon
- Insert → Icons → Tìm "robot" hoặc "chat"
- Đặt cạnh chatbot

### 3. Animation
- Thêm animation cho button
- Fade in, Fly in, etc.

### 4. Responsive
- Test trên nhiều kích thước màn hình
- Đảm bảo chatbot hiển thị tốt

---

## ✅ CHECKLIST

- [ ] Đã deploy chatbot lên server
- [ ] Có URL công khai
- [ ] Test URL trong trình duyệt
- [ ] Chèn vào PowerPoint thành công
- [ ] Test trình chiếu
- [ ] Chatbot hoạt động tốt

---

## 🆘 TROUBLESHOOTING

### Chatbot không hiển thị
- Kiểm tra URL đúng chưa
- Kiểm tra kết nối internet
- Thử mở URL trực tiếp trong trình duyệt

### Web Viewer không hoạt động
- Cài đặt lại add-in
- Thử dùng Hyperlink thay thế
- Kiểm tra PowerPoint version (cần 2016+)

### Chatbot chậm
- Lần đầu load có thể chậm (download models)
- Đợi vài giây
- Refresh lại

---

## 💡 GỢI Ý SỬ DỤNG

1. **Slide đầu**: Giới thiệu chatbot
2. **Slide giữa**: Chèn chatbot để học sinh hỏi
3. **Slide cuối**: Tổng kết và link chatbot

---

## 📱 TÍCH HỢP VÀO GOOGLE SLIDES

Nếu dùng Google Slides:
1. **Insert** → **Link**
2. Nhập URL chatbot
3. Click **Apply**
4. Khi trình chiếu, click link để mở chatbot

---

Chúc bạn thành công! 🎉

