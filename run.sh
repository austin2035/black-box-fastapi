source /app/venv/bin/activate
nohup /app/venv/bin/uvicorn main:app --port 8000 --reload  > server.log 2>&1 &
