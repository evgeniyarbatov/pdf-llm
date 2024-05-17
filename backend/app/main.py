import chromadb
import os
import logging
import sys

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from langchain_chroma import Chroma

app = FastAPI()

origins = [
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = chromadb.HttpClient(
   host=os.environ.get('DB_HOST', 'localhost')
)

class Query(BaseModel):
    question: str

@app.get("/")
def read_root():
    return {"status": "ok"}

@app.get("/healthcheck")
def health_check():
    return {"status": "ok"}

@app.post("/query")
async def query_llm(query: Query):
  db = Chroma(
      client=client,
      collection_name="pdfs",
  )
  docs = db.similarity_search(
     query.question
  )
  return {"result": docs[0].page_content}
