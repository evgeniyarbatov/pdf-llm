# PDF LLM

Allow users to query LLM with context from PDFs.

## Setup

- Install ollama

## How to run

Start ollama:

```
ollama run llama3
```

Start ChromaDB / backend / frontend:

```
docker-compose up --build
```

Seed PDFs into ChromaDB:

- place PDFs into 'documents' directory
- run: `make`

Open browser on http://localhost and enter queries.