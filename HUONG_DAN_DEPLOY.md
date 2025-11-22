# 🚀 HƯỚNG DẪN DEPLOY HOÀN CHỈNH

## ✅ ĐÃ HOÀN THÀNH

1. ✅ Tạo `chatbot_deploy.py` - phiên bản nhẹ (không load docx)
2. ✅ Sửa `server.py` - tự động detect deploy/local
3. ✅ Sửa `Procfile` - thêm timeout 120s
4. ✅ Sửa `runtime.txt` - Python 3.10.12
5. ✅ Tạo `generate_embeddings.py` - script tạo embeddings

## 📋 BƯỚC TIẾP THEO (QUAN TRỌNG!)

### Bước 1: Tạo embeddings trên LOCAL

Chạy file:
```bash
TAO_EMBEDDINGS.bat
```

Hoặc:
```bash
python generate_embeddings.py
```

Script này sẽ tạo 2 files:
- `embeddings.npy` - embeddings đã tính sẵn
- `chunks.json` - chunks text

### Bước 2: Commit và push

```bash
git add embeddings.npy chunks.json
git commit -m "Add embeddings for deploy"
git push origin main
```

### Bước 3: Deploy trên Render

1. Render sẽ tự động deploy khi push
2. Đảm bảo Environment Variable `GROQ_API_KEY` đã được set
3. Đợi deploy xong (5-10 phút)

## 🎯 KẾT QUẢ

- ✅ Deploy thành công
- ✅ Không out-of-memory
- ✅ Không load docx trên server
- ✅ Chạy ổn định 24/7
- ✅ PowerPoint embed được

## 📝 LƯU Ý

- **LOCAL**: Vẫn dùng `chatbot.py` (load docx đầy đủ)
- **DEPLOY**: Tự động dùng `chatbot_deploy.py` (nhẹ, nhanh)
- `embeddings.npy` và `chunks.json` PHẢI có trong repo để deploy chạy được!

