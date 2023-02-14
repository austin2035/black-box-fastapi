source ./venv/bin/activate
nohup  ./venv/bin/uvicorn main:app --port 2036 --reload  > server.log 2>&1 &