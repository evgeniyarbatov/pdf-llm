import chromadb

from fastapi import FastAPI
from pydantic import BaseModel

from langchain_chroma import Chroma
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)

app = FastAPI()

client = chromadb.HttpClient()
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

class Query(BaseModel):
    question: str

@app.post("/query")
async def query_llm(query: Query):
  db4 = Chroma(
      client=client,
      collection_name="pdfs",
      embedding_function=embedding_function,
  )
  docs = db4.similarity_search(
     query.question
  )
  return {"result": docs[0].page_content}