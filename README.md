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
- `Who is Mr. Kwok of Ace Holdings`

This runs very slow but it seems to work 

## UI

![screencapture-localhost-2024-05-17-17_30_26](https://github.com/evgeniyarbatov/pdf-llm/assets/1913350/125ffa78-1e78-46a9-9be5-cbe6be69ff78)
![screencapture-localhost-2024-05-17-17_39_14](https://github.com/evgeniyarbatov/pdf-llm/assets/1913350/28598e93-755b-42e2-9f7d-1e7d2898d756)



