source /app/venv/black-box/bin/activate
nohup /app/venv/black-box/bin/uvicorn main:app --port 8000 --reload  > server.log 2>&1 &
