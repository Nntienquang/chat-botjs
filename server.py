"""
Web Server cho Chatbot - Sử dụng Groq API (Llama 3.1)
"""
from flask import Flask, render_template_string, request, jsonify
from flask_cors import CORS
from chatbot import DocumentChatbot
import os
app = Flask(__name__)
CORS(app)

# Khởi tạo chatbot ngay khi start (không lazy load để đảm bảo hoạt động)
print("="*50)
print("Đang khởi tạo chatbot với Groq API (Llama 3.1)...")
try:
    chatbot = DocumentChatbot(doc_folder="doc")
    chatbot.load_documents()
    print("✅ Chatbot đã sẵn sàng!")
    print("="*50)
except Exception as e:
    print(f"❌ LỖI NGHIÊM TRỌNG: Không thể khởi tạo chatbot!")
    print(f"Chi tiết lỗi: {e}")
    import traceback
    traceback.print_exc()
    chatbot = None
    print("="*50)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chatbot Bài Giảng</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 10px;
        }
        .container {
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
            width: 100%;
            max-width: 900px;
            height: 95vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            text-align: center;
        }
        .header h2 {
            margin: 0;
            font-size: 24px;
        }
        #chatbox {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
            background: #f5f5f5;
        }
        .message {
            margin-bottom: 15px;
            padding: 12px 15px;
            border-radius: 10px;
            max-width: 80%;
            word-wrap: break-word;
            animation: fadeIn 0.3s;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .user {
            background: #667eea;
            color: white;
            margin-left: auto;
            text-align: right;
        }
        .bot {
            background: white;
            color: #333;
            border: 1px solid #ddd;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .input-area {
            padding: 20px;
            background: white;
            border-top: 1px solid #ddd;
            display: flex;
            gap: 10px;
        }
        #question {
            flex: 1;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 25px;
            font-size: 14px;
            outline: none;
        }
        #question:focus {
            border-color: #667eea;
        }
        button {
            padding: 12px 30px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            font-size: 14px;
            font-weight: bold;
            transition: transform 0.2s;
        }
        button:hover {
            transform: scale(1.05);
        }
        button:active {
            transform: scale(0.95);
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h2>🤖 Chatbot Bài Giảng</h2>
        </div>
        <div id="chatbox">
            <div class="message bot">
                <strong>Chatbot:</strong> Xin chào! Tôi đã sẵn sàng trả lời các câu hỏi về tài liệu. Hãy đặt câu hỏi của bạn!
            </div>
        </div>
        <div class="input-area">
            <input type="text" id="question" placeholder="Nhập câu hỏi của bạn..." onkeypress="handleKeyPress(event)">
            <button onclick="askQuestion()">Gửi</button>
        </div>
    </div>
    
    <script>
        function handleKeyPress(event) {
            if (event.key === 'Enter') {
                askQuestion();
            }
        }
        
        function askQuestion() {
            const questionInput = document.getElementById('question');
            const question = questionInput.value.trim();
            
            if (!question) return;
            
            const chatbox = document.getElementById('chatbox');
            
            const userMsg = document.createElement('div');
            userMsg.className = 'message user';
            userMsg.innerHTML = '<strong>Bạn:</strong> ' + question;
            chatbox.appendChild(userMsg);
            chatbox.scrollTop = chatbox.scrollHeight;
            
            questionInput.value = '';
            
            const loadingMsg = document.createElement('div');
            loadingMsg.className = 'message bot';
            loadingMsg.innerHTML = '<strong>Chatbot:</strong> Đang suy nghĩ...';
            chatbox.appendChild(loadingMsg);
            chatbox.scrollTop = chatbox.scrollHeight;
            
            fetch('/ask', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({question: question})
            })
            .then(response => response.json())
            .then(data => {
                loadingMsg.remove();
                const botMsg = document.createElement('div');
                botMsg.className = 'message bot';
                botMsg.innerHTML = '<strong>Chatbot:</strong> ' + data.answer.replace(/\\n/g, '<br>');
                chatbox.appendChild(botMsg);
                chatbox.scrollTop = chatbox.scrollHeight;
            })
            .catch(error => {
                loadingMsg.remove();
                const errorMsg = document.createElement('div');
                errorMsg.className = 'message bot';
                errorMsg.innerHTML = '<strong>Lỗi:</strong> Không thể kết nối đến chatbot.';
                chatbox.appendChild(errorMsg);
                chatbox.scrollTop = chatbox.scrollHeight;
            });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    if chatbot is None:
        return jsonify({'status': 'error', 'message': 'Chatbot chưa được khởi tạo'}), 500
    return jsonify({'status': 'ok', 'message': 'Chatbot đã sẵn sàng'}), 200

@app.route('/ask', methods=['POST'])
def ask():
    try:
        # Kiểm tra chatbot đã được khởi tạo chưa
        if chatbot is None:
            print("❌ Chatbot chưa được khởi tạo!")
            return jsonify({'answer': 'Xin lỗi, chatbot chưa sẵn sàng. Vui lòng thử lại sau.'}), 503
        
        data = request.json
        if not data:
            return jsonify({'answer': 'Xin lỗi, dữ liệu không hợp lệ.'}), 400
            
        question = data.get('question', '').strip()
        if not question:
            return jsonify({'answer': 'Xin lỗi, bạn chưa nhập câu hỏi.'}), 400
        
        print(f"📥 Nhận câu hỏi: {question[:50]}...")
        
        # Xử lý câu hỏi
        try:
            answer = chatbot.answer(question)
            print(f"✅ Trả lời thành công (độ dài: {len(answer)} ký tự)")
            return jsonify({'answer': answer})
        except Exception as e:
            print(f"❌ Lỗi khi xử lý câu hỏi: {e}")
            import traceback
            traceback.print_exc()
            return jsonify({'answer': f'Xin lỗi, đã xảy ra lỗi khi xử lý câu hỏi: {str(e)}'}), 500
            
    except Exception as e:
        print(f"❌ Lỗi trong route /ask: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'answer': f'Xin lỗi, đã xảy ra lỗi: {str(e)}'}), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    print("\n" + "="*50)
    print("Chatbot Web Server đang chạy...")
    print(f"URL: http://localhost:{port}")
    print("Để tích hợp vào PowerPoint, sử dụng URL trên")
    print("Nhấn Ctrl+C để dừng server")
    print("="*50 + "\n")
    app.run(host='0.0.0.0', port=port, debug=False)

