@echo off
echo ========================================
echo Tao embeddings cho deploy
echo ========================================
echo.

if exist "C:\Users\%USERNAME%\anaconda3\python.exe" (
    C:\Users\%USERNAME%\anaconda3\python.exe generate_embeddings.py
) else if exist "C:\ProgramData\anaconda3\python.exe" (
    C:\ProgramData\anaconda3\python.exe generate_embeddings.py
) else (
    python generate_embeddings.py
)

pause

