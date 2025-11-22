"""
Chatbot sử dụng Groq API (Llama 3.1)
Bản TỐI ƯU deploy – KHÔNG load docx, KHÔNG tạo embedding
Chỉ đọc 2 file: embeddings.npy + chunks.json
"""
import os
import json
import numpy as np
from groq import Groq
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re
from typing import List, Tuple, Optional
from dotenv import load_dotenv

# Load biến môi trường từ file .env
load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")

class DocumentChatbot:
    def __init__(self):
        """Khởi tạo chatbot - phiên bản deploy (nhẹ)"""
        # Khởi tạo Groq client
        if not GROQ_API_KEY:
            print("❌ GROQ_API_KEY chưa được set!")
            print("   Kiểm tra: Render → Settings → Environment Variables")
            self.groq_client = None
        else:
            try:
                self.groq_client = Groq(api_key=GROQ_API_KEY)
                print("✅ Đã kết nối Groq API")
            except Exception as e:
                print(f"❌ Lỗi kết nối Groq API: {e}")
                self.groq_client = None
        
        # Load embeddings và chunks (đã tạo sẵn từ local)
        print("🔄 Đang load embeddings (deploy version)...")
        try:
            self.chunks = json.load(open("chunks.json", encoding="utf-8"))
            # Load embeddings với mmap_mode để tiết kiệm memory
            self.embeddings = np.load("embeddings.npy", mmap_mode='r')
            print(f"✅ Loaded {len(self.chunks)} chunks & embeddings shape: {self.embeddings.shape} (memory-mapped)")
        except FileNotFoundError as e:
            print(f"❌ Không tìm thấy embeddings.npy hoặc chunks.json!")
            print(f"   Lỗi: {e}")
            print("   Vui lòng chạy generate_embeddings.py trên local trước!")
            self.chunks = []
            self.embeddings = None
        except Exception as e:
            print(f"❌ Lỗi khi load embeddings: {e}")
            self.chunks = []
            self.embeddings = None
        
        # KHÔNG load model ngay - lazy load khi cần
        self.model = None
        print("✅ Embeddings đã sẵn sàng (model sẽ load khi cần)")
        
        # Load Q&A dataset nếu có
        self.load_qa_dataset()
    
    def load_qa_dataset(self):
        """Tải Q&A dataset"""
        try:
            if os.path.exists("qa_dataset.json"):
                with open("qa_dataset.json", 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.qa_dataset = data.get('questions', [])
                    print(f"✅ Đã tải {len(self.qa_dataset)} Q&A từ dataset")
            else:
                self.qa_dataset = []
        except Exception as e:
            print(f"⚠️ Không thể load Q&A dataset: {e}")
            self.qa_dataset = []
    
    def find_qa_match(self, question: str) -> Optional[str]:
        """Tìm trong Q&A dataset"""
        if not self.qa_dataset:
            return None
        
        question_lower = question.lower().strip()
        
        # Tìm chính xác
        for qa in self.qa_dataset:
            if qa['question'].lower().strip() == question_lower:
                return qa['answer']
        
        # Tìm theo keyword
        question_words = set(re.findall(r'\b\w{2,}\b', question_lower))
        best_match = None
        best_score = 0
        
        for qa in self.qa_dataset:
            qa_keywords = set(qa.get('keywords', []))
            keyword_match = len(question_words & qa_keywords)
            if keyword_match > best_score and keyword_match > 0:
                best_score = keyword_match
                best_match = qa['answer']
        
        return best_match if best_score > 1 else None
    
    def _get_model(self):
        """Lazy load model - chỉ load khi cần"""
        if self.model is None:
            print("🔄 Lazy loading model embedding...")
            try:
                self.model = SentenceTransformer("all-MiniLM-L6-v2")
                print("✅ Model đã sẵn sàng")
            except Exception as e:
                print(f"❌ Lỗi khi load model: {e}")
                return None
        return self.model
    
    def search(self, query: str, top_k: int = 5) -> List[Tuple[str, float]]:
        """Tìm kiếm semantic"""
        if not self.chunks or self.embeddings is None:
            return []
        
        model = self._get_model()
        if model is None:
            return []
        
        try:
            # Encode query
            q_emb = model.encode([query], show_progress_bar=False)
            # Tính similarity với memory-mapped embeddings
            sim = cosine_similarity(q_emb, self.embeddings)[0]
            idx = np.argsort(sim)[::-1][:top_k]
            
            results = []
            for i in idx:
                if sim[i] > 0.15:  # Ngưỡng tối thiểu
                    results.append((self.chunks[i], float(sim[i])))
            return results
        except Exception as e:
            print(f"❌ Lỗi khi search: {e}")
            return []
    
    def build_context(self, question: str) -> str:
        """Xây dựng context từ kết quả tìm kiếm"""
        results = self.search(question, top_k=5)
        if not results:
            return ""
        
        parts = []
        for chunk, score in results:
            if score > 0.15:
                parts.append(chunk)
        
        return "\n\n---\n\n".join(parts) if parts else ""
    
    def call_groq(self, question: str, context: str) -> str:
        """Gọi Groq API"""
        if not self.groq_client:
            return "Xin lỗi, chatbot chưa được cấu hình đúng. Vui lòng kiểm tra GROQ_API_KEY."
        
        if not context:
            return "Xin lỗi, tôi không tìm thấy thông tin về câu hỏi này trong tài liệu."
        
        try:
            system_msg = """Bạn là chatbot bài giảng thông minh. Nhiệm vụ của bạn là đọc kỹ thông tin tài liệu và trả lời câu hỏi một cách CHÍNH XÁC, ĐẦY ĐỦ, TỰ NHIÊN và MẠCH LẠC.

QUY TẮC NGHIÊM NGẶT:
1. CHỈ trả lời dựa trên thông tin CÓ SẴN trong tài liệu được cung cấp
2. KHÔNG được thêm bất kỳ thông tin nào không có trong tài liệu
3. Nếu tài liệu không có thông tin để trả lời, hãy nói rõ "Tài liệu không có thông tin về..."
4. Trả lời đầy đủ, rõ ràng, mạch lạc nhưng TUYỆT ĐỐI không thêm thông tin ngoài"""
            
            user_msg = f"""ĐÂY LÀ TOÀN BỘ THÔNG TIN TÀI LIỆU (CHỈ DỰA VÀO ĐÂY ĐỂ TRẢ LỜI):

{context[:3000]}

---
CÂU HỎI: {question}

LƯU Ý QUAN TRỌNG:
- CHỈ trả lời dựa trên thông tin TRÊN ĐÂY
- Nếu thông tin không có trong tài liệu trên, hãy nói rõ "Tài liệu không có thông tin về..."
- KHÔNG được suy đoán, tưởng tượng, hoặc thêm thông tin ngoài

TRẢ LỜI (chỉ dựa trên tài liệu):"""
            
            res = self.groq_client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": user_msg}
                ],
                temperature=0.3,
                max_tokens=600
            )
            
            return res.choices[0].message.content.strip()
        except Exception as e:
            print(f"❌ Lỗi khi gọi Groq API: {e}")
            return f"Xin lỗi, đã xảy ra lỗi khi xử lý câu hỏi: {str(e)}"
    
    def answer(self, question: str) -> str:
        """Trả lời câu hỏi"""
        question = question.strip()
        
        if len(question) < 3:
            return "Xin lỗi, câu hỏi của bạn quá ngắn. Vui lòng đặt câu hỏi cụ thể hơn."
        
        # Tìm trong Q&A dataset trước
        qa_answer = self.find_qa_match(question)
        if qa_answer:
            return qa_answer
        
        # Tìm context và gọi Groq API
        context = self.build_context(question)
        answer = self.call_groq(question, context)
        
        return answer

