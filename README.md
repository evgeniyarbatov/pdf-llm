# PDF LLM

Allow users to query LLM with context from PDFs.

## Setup

- Install LMStudio 
- Download `Llama 3 - 8B Instruct` model

## How to run

Start local server in LMStudio.

Start ChromaDB / backend / frontend:

```
docker compose up 
```

Seed PDFs into ChromaDB:

- place PDFs into 'documents' directory
- run: `make`

Open browser on http://localhost and enter queries.