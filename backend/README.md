# Backend

FastAPI backend to query ChromaDB and LLM

## Dev

Init:

```
python3.12 -m venv ~/.venv/pdf-llm-backend
source ~/.venv/pdf-llm-backend/bin/activate
```

Install deps:

```
pip install -r app/requirements.txt
```

Run

```
uvicorn app.main:app --port 9000 --reload
```