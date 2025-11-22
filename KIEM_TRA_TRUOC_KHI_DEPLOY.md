# ✅ CHECKLIST TRƯỚC KHI DEPLOY

## 📁 Files cần có

- [ ] `chatbot.py` - File chính
- [ ] `server.py` - Web server
- [ ] `requirements.txt` - Dependencies
- [ ] `Procfile` - Cấu hình cho Render/Heroku
- [ ] `runtime.txt` - Phiên bản Python
- [ ] `qa_dataset.json` - Q&A dataset
- [ ] Folder `doc/` - Tài liệu (với files bên trong)
- [ ] `.gitignore` - (Tùy chọn)

## 🔍 Kiểm tra nội dung

### requirements.txt
- [ ] Có `flask`
- [ ] Có `gunicorn`
- [ ] Có `sentence-transformers`
- [ ] Có `python-docx`
- [ ] Có `PyPDF2`
- [ ] Có `scikit-learn`
- [ ] Có `flask-cors`

### Procfile
- [ ] Nội dung: `web: gunicorn server:app`

### runtime.txt
- [ ] Nội dung: `python-3.10.11` (hoặc phiên bản Python bạn dùng)

### server.py
- [ ] Có `host='0.0.0.0'`
- [ ] Có `port=os.environ.get('PORT', 5000)`

### Folder doc/
- [ ] Có ít nhất 1 file tài liệu (.docx, .pdf, hoặc .txt)
- [ ] Files không quá lớn (< 10MB mỗi file)

## 🧪 Test local

- [ ] Chạy `CHAY.bat` thành công
- [ ] Chatbot trả lời được câu hỏi
- [ ] Không có lỗi trong console

## 📤 Chuẩn bị GitHub

- [ ] Đã tạo GitHub account
- [ ] Đã tạo repository
- [ ] Đã upload tất cả files

## ✅ Sau khi deploy

- [ ] Service build thành công
- [ ] URL hoạt động
- [ ] Chatbot trả lời được
- [ ] Tích hợp vào PowerPoint thành công

---

**Nếu tất cả đều ✅ → Sẵn sàng deploy!**

