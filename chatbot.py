"""
Chatbot sử dụng Groq API (Llama 3.1) để trả lời câu hỏi về tài liệu
"""
import os
import json
import re
from typing import List, Tuple, Optional
from docx import Document
import PyPDF2
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from groq import Groq

# Groq API (FREE - Llama 3.1)
# Lấy từ biến môi trường (bắt buộc)
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")

class DocumentChatbot:
    def __init__(self, doc_folder: str = "doc"):
        """
        Khởi tạo chatbot với Groq API (Llama 3.1)
        """
        self.doc_folder = doc_folder
        self.documents = []
        self.document_metadata = []
        self.chunks = []
        self.embeddings = None
        self.model = None
        
        # Khởi tạo Groq client
        try:
            self.groq_client = Groq(api_key=GROQ_API_KEY)
            print(f"✓ Đã kết nối Groq API thành công! (Key: {GROQ_API_KEY[:10]}...)")
        except Exception as e:
            print(f"❌ Lỗi kết nối Groq API: {e}")
            self.groq_client = None
        
        print("Đang tải mô hình embedding...")
        try:
            self.model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
        except:
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
        print("✓ Đã tải mô hình embedding thành công!")
        
        # Tải Q&A dataset nếu có
        self.load_qa_dataset()
        
        print("Chatbot đã sẵn sàng với Groq API (Llama 3.1)!")
    
    def load_qa_dataset(self):
        """Tải Q&A dataset"""
        qa_file = "qa_dataset.json"
        if os.path.exists(qa_file):
            try:
                with open(qa_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.qa_dataset = data.get('questions', [])
                    print(f"✓ Đã tải {len(self.qa_dataset)} câu hỏi-đáp từ dataset!")
            except Exception as e:
                print(f"Không thể tải Q&A dataset: {e}")
                self.qa_dataset = []
        else:
            self.qa_dataset = []
    
    def read_docx(self, file_path: str) -> str:
        """Đọc file .docx"""
        try:
            doc = Document(file_path)
            text = []
            
            for paragraph in doc.paragraphs:
                if paragraph.text.strip():
                    text.append(paragraph.text.strip())
            
            # Đọc tables
            for table in doc.tables:
                for row in table.rows:
                    row_text = []
                    for cell in row.cells:
                        if cell.text.strip():
                            row_text.append(cell.text.strip())
                    if row_text:
                        text.append(" | ".join(row_text))
            
            return "\n\n".join(text)
        except Exception as e:
            print(f"Lỗi đọc file {file_path}: {e}")
            return ""
    
    def read_pdf(self, file_path: str) -> str:
        """Đọc file .pdf"""
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = []
                for page in pdf_reader.pages:
                    text.append(page.extract_text())
                return "\n\n".join(text)
        except Exception as e:
            print(f"Lỗi đọc file {file_path}: {e}")
            return ""
    
    def read_txt(self, file_path: str) -> str:
        """Đọc file .txt"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Lỗi đọc file {file_path}: {e}")
            return ""
    
    def load_documents(self):
        """Đọc tất cả tài liệu từ folder doc"""
        if not os.path.exists(self.doc_folder):
            print(f"Folder {self.doc_folder} không tồn tại!")
            return
        
        print(f"Đang đọc tài liệu từ folder {self.doc_folder}...")
        
        import glob
        docx_files = glob.glob(os.path.join(self.doc_folder, "*.docx"))
        pdf_files = glob.glob(os.path.join(self.doc_folder, "*.pdf"))
        txt_files = glob.glob(os.path.join(self.doc_folder, "*.txt"))
        
        all_files = docx_files + pdf_files + txt_files
        
        for file_path in all_files:
            file_name = os.path.basename(file_path)
            if file_name.startswith("~$"):  # Bỏ qua file temp
                continue
            
            print(f"Đang đọc: {file_name}")
            
            if file_path.endswith('.docx'):
                content = self.read_docx(file_path)
            elif file_path.endswith('.pdf'):
                content = self.read_pdf(file_path)
            elif file_path.endswith('.txt'):
                content = self.read_txt(file_path)
            else:
                continue
            
            if content.strip():
                # Chia thành chunks
                chunks = self.split_text(content)
                for chunk in chunks:
                    self.chunks.append(chunk)
                    self.document_metadata.append({
                        'file': file_name,
                        'path': file_path
                    })
        
        print(f"Đã đọc {len(self.chunks)} chunks từ {len(all_files)} files")
        
        # Tạo embeddings
        if self.chunks:
            print("Đang tạo embeddings...")
            self.embeddings = self.model.encode(self.chunks, show_progress_bar=True)
            print("✓ Đã tạo embeddings thành công!")
    
    def split_text(self, text: str, chunk_size: int = 800) -> List[str]:
        """Chia text thành chunks"""
        # Chia theo đoạn văn trước
        paragraphs = re.split(r'\n\s*\n', text)
        chunks = []
        current_chunk = ""
        
        for para in paragraphs:
            para = para.strip()
            if not para:
                continue
            
            if len(current_chunk) + len(para) < chunk_size:
                current_chunk += "\n\n" + para if current_chunk else para
            else:
                if current_chunk:
                    chunks.append(current_chunk)
                current_chunk = para
        
        if current_chunk:
            chunks.append(current_chunk)
        
        return chunks
    
    def search(self, query: str, top_k: int = 5) -> List[Tuple[str, float]]:
        """Tìm kiếm semantic trong tài liệu"""
        if not self.chunks or self.embeddings is None:
            return []
        
        query_embedding = self.model.encode([query])
        similarities = cosine_similarity(query_embedding, self.embeddings)[0]
        
        # Lấy top_k kết quả
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        results = []
        for idx in top_indices:
            if similarities[idx] > 0.15:  # Ngưỡng tối thiểu (giảm để lấy nhiều kết quả hơn)
                results.append((self.chunks[idx], float(similarities[idx])))
        
        return results
    
    def search_context(self, query: str, max_chunks: int = 5) -> str:
        """Tìm và kết hợp các đoạn liên quan nhất để làm context"""
        # Tăng số chunks để có đủ context
        results = self.search(query, top_k=max_chunks)
        
        if not results:
            return ""
        
        # Kết hợp các chunks theo độ liên quan, có điểm số để ưu tiên
        context_parts = []
        for chunk, score in results:
            # Chỉ lấy chunks có độ liên quan đủ cao
            if score > 0.2:  # Ngưỡng tối thiểu
                context_parts.append(f"[Độ liên quan: {score:.2f}]\n{chunk}")
        
        if not context_parts:
            # Nếu không có chunk nào đủ điểm, vẫn lấy chunk tốt nhất
            context_parts.append(results[0][0])
        
        return "\n\n---\n\n".join(context_parts)
    
    def find_qa_match(self, question: str) -> Optional[str]:
        """Tìm câu trả lời từ Q&A dataset"""
        if not self.qa_dataset:
            return None
        
        question_lower = question.lower().strip()
        
        # Tìm kiếm chính xác
        for qa in self.qa_dataset:
            if qa['question'].lower().strip() == question_lower:
                return qa['answer']
        
        # Tìm kiếm theo từ khóa
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
    
    def call_groq_api(self, question: str, context: str = "") -> Optional[str]:
        """Gọi Groq API (Llama 3.1) để tạo câu trả lời - CHỈ dựa trên tài liệu"""
        if not self.groq_client:
            print("❌ Groq client chưa được khởi tạo!")
            return None
        
        if not context or len(context.strip()) < 10:
            print("⚠️ Context quá ngắn, không đủ để trả lời")
            return None
        
        try:
            # Giới hạn context để tránh quá dài, nhưng đảm bảo đủ thông tin
            context_limited = context[:4000] if len(context) > 4000 else context
            
            print(f"🔄 Đang gọi Groq API với câu hỏi: {question[:50]}...")
            print(f"📄 Context length: {len(context_limited)} ký tự")
            
            # Prompt rất nghiêm ngặt để bắt buộc chỉ trả lời dựa trên tài liệu
            system_prompt = """Bạn là chatbot bài giảng. QUY TẮC NGHIÊM NGẶT:
1. CHỈ trả lời dựa trên thông tin CÓ SẴN trong tài liệu được cung cấp
2. KHÔNG được thêm bất kỳ thông tin nào không có trong tài liệu
3. Nếu tài liệu không có thông tin để trả lời, hãy nói rõ "Tài liệu không có thông tin về..."
4. Trích dẫn chính xác từ tài liệu khi có thể
5. Trả lời đầy đủ, rõ ràng, mạch lạc nhưng TUYỆT ĐỐI không thêm thông tin ngoài"""
            
            user_prompt = f"""ĐÂY LÀ TOÀN BỘ THÔNG TIN TÀI LIỆU (CHỈ DỰA VÀO ĐÂY ĐỂ TRẢ LỜI):

{context_limited}

---
CÂU HỎI: {question}

LƯU Ý QUAN TRỌNG:
- CHỈ trả lời dựa trên thông tin TRÊN ĐÂY
- Nếu thông tin không có trong tài liệu trên, hãy nói rõ "Tài liệu không có thông tin về..."
- KHÔNG được suy đoán, tưởng tượng, hoặc thêm thông tin ngoài
- Trích dẫn chính xác từ tài liệu khi có thể

TRẢ LỜI (chỉ dựa trên tài liệu):"""
            
            # Gọi Groq API với Llama 3.1 - giảm temperature để chính xác hơn
            completion = self.groq_client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ],
                temperature=0.3,  # Giảm từ 0.7 xuống 0.3 để chính xác hơn, ít "tưởng tượng" hơn
                max_tokens=600
            )
            
            answer = completion.choices[0].message.content.strip()
            print(f"✅ Groq API trả lời thành công! (Độ dài: {len(answer)} ký tự)")
            
            # Kiểm tra xem câu trả lời có quá ngắn không
            if answer and len(answer) > 15:
                # Làm sạch câu trả lời
                answer = answer.strip()
                # Loại bỏ các phần có thể là prompt còn sót lại
                if "TRẢ LỜI:" in answer:
                    answer = answer.split("TRẢ LỜI:")[-1].strip()
                return answer
            
            print("⚠️ Câu trả lời từ Groq API quá ngắn")
            return None
                
        except Exception as e:
            print(f"❌ Lỗi khi gọi Groq API: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def answer(self, question: str) -> str:
        """Trả lời câu hỏi sử dụng Groq API"""
        question = question.strip()
        
        if len(question) < 3:
            return "Xin lỗi, câu hỏi của bạn quá ngắn. Vui lòng đặt câu hỏi cụ thể hơn."
        
        # Tìm trong Q&A dataset trước (nhưng vẫn log để debug)
        qa_answer = self.find_qa_match(question)
        if qa_answer:
            print(f"📚 Tìm thấy trong Q&A dataset, bỏ qua API call")
            return qa_answer
        
        # Tìm kiếm context liên quan nhất - tăng số chunks để có đủ thông tin
        context = self.search_context(question, max_chunks=5)
        
        if not context:
            return f"Xin lỗi, tôi không tìm thấy thông tin về '{question}' trong tài liệu. Hãy thử đặt câu hỏi khác."
        
        print(f"📚 Đã tìm thấy context từ tài liệu ({len(context)} ký tự)")
        
        # Gọi Groq API (Llama 3.1) để tạo câu trả lời
        answer = self.call_groq_api(question, context)
        
        if answer and len(answer) > 20:
            # Làm sạch câu trả lời
            answer = answer.strip()
            # Loại bỏ các ký tự lạ
            answer = re.sub(r'\s+', ' ', answer)
            return answer
        
        # Fallback: Tổng hợp từ các chunks tốt nhất
        results = self.search(question, top_k=3)
        if results:
            if len(results) > 1:
                combined = "\n\n".join([chunk for chunk, score in results[:2]])
                return f"Dựa trên tài liệu:\n\n{combined[:500]}..."
            else:
                return results[0][0][:500] + "..." if len(results[0][0]) > 500 else results[0][0]
        
        return f"Xin lỗi, tôi không tìm thấy thông tin về '{question}' trong tài liệu."

