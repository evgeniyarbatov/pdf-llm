import chromadb
from chromadb.config import Settings

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)

import sys
import os
import uuid

def get_documents(path):
    documents = []
    for file in os.listdir(path):
        if file.endswith('.pdf'):
            pdf_path = os.path.join(path, file)
            loader = PyPDFLoader(pdf_path)
            documents.extend(loader.load())
    return documents

def main(args):
  documents_path = args[0]
  
  client = chromadb.HttpClient(settings=Settings(allow_reset=True))
  client.reset()  # resets the database
  collection = client.create_collection("pdfs")

  docs = get_documents(documents_path)
  for doc in docs:
    collection.add(
        ids=[str(uuid.uuid1())], metadatas=doc.metadata, documents=doc.page_content
    )

if __name__ == "__main__":
    main(sys.argv[1:])
