# 🌐 CÁC NỀN TẢNG DEPLOY MIỄN PHÍ

## 1. 🚀 Railway.app (Khuyến nghị - Dễ nhất)

### Ưu điểm:
- ✅ Tự động detect Python
- ✅ Không cần Procfile (tự động detect)
- ✅ Deploy nhanh
- ✅ Free tier tốt

### Cách deploy:
1. Vào https://railway.app → Sign up với GitHub
2. **New Project** → **Deploy from GitHub repo**
3. Chọn repository `chatbot-bai-giang`
4. Railway tự động detect và deploy!
5. Đợi 3-5 phút

### Cấu hình (nếu cần):
- **Start Command**: `gunicorn server:app --bind 0.0.0.0:$PORT`
- Railway tự động set PORT

### URL:
- Dạng: `https://chatbot-bai-giang.up.railway.app`

---

## 2. ☁️ PythonAnywhere

### Ưu điểm:
- ✅ Miễn phí cho Python web apps
- ✅ Dễ sử dụng
- ✅ Không cần Git

### Cách deploy:
1. Đăng ký: https://www.pythonanywhere.com
2. Vào **Web** tab → **Add a new web app**
3. Chọn **Flask**, Python 3.10
4. Upload files qua **Files** tab
5. Cấu hình WSGI file:
```python
import sys
path = '/home/yourusername/mysite'
if path not in sys.path:
    sys.path.append(path)

from server import app as application
```
6. Reload web app

### URL:
- Dạng: `https://yourusername.pythonanywhere.com`

---

## 3. 🔷 Fly.io

### Ưu điểm:
- ✅ Free tier tốt
- ✅ Global edge network
- ✅ Nhanh

### Cách deploy:
1. Cài Fly CLI: https://fly.io/docs/getting-started/installing-flyctl/
2. Đăng ký: `fly auth signup`
3. Tạo file `fly.toml`:
```toml
app = "chatbot-bai-giang"
primary_region = "sin"

[build]

[env]
  PORT = "8080"

[[services]]
  http_checks = []
  internal_port = 8080
  processes = ["app"]
  protocol = "tcp"
  script_checks = []

  [services.concurrency]
    hard_limit = 25
    soft_limit = 20
    type = "connections"

  [[services.ports]]
    force_https = true
    handlers = ["http"]
    port = 80

  [[services.ports]]
    handlers = ["tls", "http"]
    port = 443

  [[services.tcp_checks]]
    grace_period = "1s"
    interval = "15s"
    restart_limit = 0
    timeout = "2s"
```

4. Deploy: `fly deploy`

### URL:
- Dạng: `https://chatbot-bai-giang.fly.dev`

---

## 4. 🟢 Heroku (Có thể mất phí)

### Ưu điểm:
- ✅ Phổ biến
- ✅ Dễ dùng
- ⚠️ Free tier đã bị gỡ (có thể mất phí)

### Cách deploy:
1. Cài Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli
2. Login: `heroku login`
3. Tạo app: `heroku create chatbot-bai-giang`
4. Deploy: `git push heroku main`

---

## 5. 🟡 Replit

### Ưu điểm:
- ✅ Code trực tiếp trên web
- ✅ Free tier
- ✅ Dễ dùng

### Cách deploy:
1. Vào https://replit.com
2. **Create Repl** → **Import from GitHub**
3. Chọn repository
4. Chạy: `gunicorn server:app --bind 0.0.0.0:8080`
5. Deploy → **Deploy as Web App**

---

## 6. 🔵 Vercel (Cho Flask)

### Ưu điểm:
- ✅ Nhanh
- ✅ Free tier tốt
- ⚠️ Cần cấu hình đặc biệt cho Flask

### Cách deploy:
1. Vào https://vercel.com
2. Import GitHub repository
3. Cấu hình:
   - **Framework Preset**: Other
   - **Build Command**: `pip install -r requirements.txt`
   - **Output Directory**: (để trống)
4. Tạo file `vercel.json`:
```json
{
  "version": 2,
  "builds": [
    {
      "src": "server.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "server.py"
    }
  ]
}
```

---

## 7. 🟣 Cyclic.sh

### Ưu điểm:
- ✅ Free tier
- ✅ Tự động deploy từ GitHub
- ✅ Dễ dùng

### Cách deploy:
1. Vào https://cyclic.sh
2. Sign up với GitHub
3. **New App** → Chọn repository
4. Tự động deploy!

---

## 📊 SO SÁNH NHANH

| Nền tảng | Độ khó | Free Tier | Tốc độ | Khuyến nghị |
|----------|--------|-----------|--------|-------------|
| **Railway** | ⭐ Dễ | ✅ Tốt | ⚡ Nhanh | ⭐⭐⭐⭐⭐ |
| **Render** | ⭐ Dễ | ✅ OK | ⚡ Nhanh | ⭐⭐⭐⭐ |
| **PythonAnywhere** | ⭐⭐ Trung bình | ✅ Tốt | ⚡ Trung bình | ⭐⭐⭐ |
| **Fly.io** | ⭐⭐⭐ Khó | ✅ Tốt | ⚡⚡ Rất nhanh | ⭐⭐⭐⭐ |
| **Replit** | ⭐ Dễ | ✅ OK | ⚡ Trung bình | ⭐⭐⭐ |
| **Cyclic** | ⭐ Dễ | ✅ OK | ⚡ Nhanh | ⭐⭐⭐⭐ |

---

## 🎯 KHUYẾN NGHỊ

### Nếu Render không hoạt động:
1. **Railway.app** - Dễ nhất, tự động detect
2. **Cyclic.sh** - Tương tự Railway
3. **PythonAnywhere** - Ổn định, miễn phí

### Nếu muốn nhanh nhất:
- **Fly.io** - Edge network, rất nhanh

---

## 📝 LƯU Ý CHUNG

Tất cả các nền tảng đều cần:
- ✅ File `requirements.txt`
- ✅ File `server.py` hoặc `app.py`
- ✅ Folder `doc/` với tài liệu
- ✅ File `qa_dataset.json`

Một số cần thêm:
- `Procfile` (Render, Heroku)
- `runtime.txt` (Render)
- Cấu hình đặc biệt (Vercel, Fly.io)

---

**Chọn nền tảng phù hợp và deploy thôi! 🚀**

