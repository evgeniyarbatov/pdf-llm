# PDF LLM

Allow users to query LLM with context from PDFs.

## Setup

- Install Docker Desktop

## How to run

Start ollama / db / backend / frontend:

```
docker-compose up --build
```

Seed PDFs into db:

- place PDFs into 'documents' directory
- run: `make`

Open browser on http://localhost and enter queries.