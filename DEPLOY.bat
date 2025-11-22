@echo off
chcp 65001 >nul
echo ========================================
echo   DEPLOY CHATBOT BÀI GIẢNG
echo ========================================
echo.

echo [1/4] Kiểm tra files cần thiết...
echo.

set MISSING=0

if not exist "chatbot.py" (
    echo [X] Thiếu: chatbot.py
    set MISSING=1
) else (
    echo [✓] chatbot.py
)

if not exist "server.py" (
    echo [X] Thiếu: server.py
    set MISSING=1
) else (
    echo [✓] server.py
)

if not exist "requirements.txt" (
    echo [X] Thiếu: requirements.txt
    set MISSING=1
) else (
    echo [✓] requirements.txt
)

if not exist "Procfile" (
    echo [X] Thiếu: Procfile
    set MISSING=1
) else (
    echo [✓] Procfile
)

if not exist "runtime.txt" (
    echo [X] Thiếu: runtime.txt
    set MISSING=1
) else (
    echo [✓] runtime.txt
)

if not exist "qa_dataset.json" (
    echo [X] Thiếu: qa_dataset.json
    set MISSING=1
) else (
    echo [✓] qa_dataset.json
)

if not exist "doc\" (
    echo [X] Thiếu: folder doc/
    set MISSING=1
) else (
    echo [✓] folder doc/
)

echo.
if %MISSING%==1 (
    echo ========================================
    echo LỖI: Thiếu một số files cần thiết!
    echo Vui lòng kiểm tra lại.
    echo ========================================
    pause
    exit /b 1
)

echo [2/4] Kiểm tra nội dung files...
echo.

findstr /C:"gunicorn" requirements.txt >nul
if %ERRORLEVEL% NEQ 0 (
    echo [X] requirements.txt thiếu gunicorn
    set MISSING=1
) else (
    echo [✓] requirements.txt có gunicorn
)

findstr /C:"web: gunicorn" Procfile >nul
if %ERRORLEVEL% NEQ 0 (
    echo [X] Procfile không đúng format
    set MISSING=1
) else (
    echo [✓] Procfile đúng format
)

echo.
if %MISSING%==1 (
    echo ========================================
    echo LỖI: Một số files không đúng!
    echo Vui lòng kiểm tra lại.
    echo ========================================
    pause
    exit /b 1
)

echo [3/4] Hướng dẫn deploy...
echo.
echo ========================================
echo   CÁC BƯỚC DEPLOY:
echo ========================================
echo.
echo 1. Tạo GitHub repository:
echo    - Vào https://github.com/new
echo    - Tạo repository mới: chatbot-bai-giang
echo.
echo 2. Upload files lên GitHub:
echo    - Upload tất cả files trong folder này
echo    - Bao gồm: chatbot.py, server.py, requirements.txt,
echo      Procfile, runtime.txt, qa_dataset.json, folder doc/
echo.
echo 3. Deploy trên Render.com:
echo    - Vào https://render.com
echo    - Sign up với GitHub
echo    - New → Web Service
echo    - Connect repository
echo    - Build Command: pip install -r requirements.txt
echo    - Start Command: gunicorn server:app --bind 0.0.0.0:$PORT
echo    - Click Create Web Service
echo.
echo 4. Đợi deploy xong (5-10 phút)
echo.
echo 5. Copy URL và tích hợp vào PowerPoint
echo.
echo ========================================
echo.

echo [4/4] Mở hướng dẫn chi tiết?
choice /C YN /M "Bạn có muốn mở file hướng dẫn chi tiết không"
if errorlevel 2 goto :end
if errorlevel 1 (
    if exist "DEPLOY_STEP_BY_STEP.md" (
        start notepad DEPLOY_STEP_BY_STEP.md
    )
)

:end
echo.
echo ========================================
echo   Hoàn tất kiểm tra!
echo ========================================
echo.
echo Xem file DEPLOY_STEP_BY_STEP.md để biết chi tiết
echo.
pause

