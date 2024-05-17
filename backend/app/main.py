import chromadb
import os

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from langchain_core.prompts import PromptTemplate
from langchain.llms import Ollama
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)

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

db_client = chromadb.HttpClient(
   host=os.environ.get('DB_HOST', 'localhost')
)

llm = Ollama(model="llama3")

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
  embedding_function = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
  )

  db = Chroma(
      client=db_client,
      collection_name="pdfs",
       embedding_function=embedding_function,
  )

  template = """
  ### System:
  You are an respectful and honest assistant. You have to answer the user's questions using only the context \
  provided to you. If you don't know the answer, just say you don't know. Don't try to make up an answer.

  ### Context:
  {context}

  ### User:
  {question}

  ### Response:
  """

  qa = RetrievalQA.from_chain_type(
      llm=llm,
      retriever=db.as_retriever(),
      chain_type="stuff",
      return_source_documents=True, 
      chain_type_kwargs={'prompt': PromptTemplate.from_template(template) } 
  )

  response = qa({'query': query.question})

  return {"result": response['result']}
