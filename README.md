# PDF LLM

Allow users to query LLM with context from PDFs.

## Setup

- Install Docker Desktop
- Increase memory available for containers to at least 4GB (ollama requirement)

## How to run

Start ollama / db / backend / frontend:

```
docker-compose up --build
```

Install llama3 to ollama container:

```
docker exec ollama ollama pull llama3
```

Seed PDFs into db:

- place PDFs into 'documents' directory
- run: `make`

Open browser on http://localhost and enter queries.

Enter queries like:

- `Tell me about Ace Decade Holdings`
- `Who is Mr. Kwok`

This runs very slow but it seems to work 