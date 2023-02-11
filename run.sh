source ./venv/bin/activate
nohup  ./venv/bin/uvicorn main:app --port 8000 --reload  > server.log 2>&1 &