"""
Script chạy LOCAL để tạo embeddings.npy và chunks.json
Chạy 1 lần duy nhất, sau đó upload 2 file này lên GitHub
"""
import os
import json
import numpy as np
from docx import Document
from sentence_transformers import SentenceTransformer
import re

print("="*50)
print("TẠO EMBEDDINGS CHO DEPLOY")
print("="*50)

# 1. Đọc tài liệu
print("\n1. Đang đọc tài liệu từ doc/...")
doc_folder = "doc"
chunks = []

for file_name in os.listdir(doc_folder):
    if file_name.endswith('.docx') and not file_name.startswith('~$'):
        file_path = os.path.join(doc_folder, file_name)
        print(f"   Đang đọc: {file_name}")
        
        doc = Document(file_path)
        text = []
        for para in doc.paragraphs:
            if para.text.strip():
                text.append(para.text.strip())
        
        # Chia thành chunks
        content = "\n\n".join(text)
        paragraphs = re.split(r'\n\s*\n', content)
        current_chunk = ""
        
        for para in paragraphs:
            para = para.strip()
            if not para:
                continue
            if len(current_chunk) + len(para) < 800:
                current_chunk += "\n\n" + para if current_chunk else para
            else:
                if current_chunk:
                    chunks.append(current_chunk)
                current_chunk = para
        
        if current_chunk:
            chunks.append(current_chunk)

print(f"   ✓ Đã tạo {len(chunks)} chunks")

# 2. Tạo embeddings
print("\n2. Đang tạo embeddings...")
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(chunks, show_progress_bar=True)
print(f"   ✓ Đã tạo embeddings: {embeddings.shape}")

# 3. Lưu file
print("\n3. Đang lưu files...")
np.save("embeddings.npy", embeddings)
with open("chunks.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, ensure_ascii=False, indent=2)

print("\n" + "="*50)
print("✅ HOÀN TẤT!")
print("="*50)
print("\nĐã tạo 2 files:")
print("  - embeddings.npy")
print("  - chunks.json")
print("\n👉 Bây giờ commit và push 2 files này lên GitHub!")

