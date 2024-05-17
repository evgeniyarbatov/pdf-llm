import chromadb
from chromadb.config import Settings

from langchain_community.document_loaders import PyPDFLoader

import sys
import os
import uuid

def get_documents(path):
    documents = []
    for file in os.listdir(path):
        if file.endswith('.pdf'):
            print('Loading:', file)
            pdf_path = os.path.join(path, file)
            loader = PyPDFLoader(pdf_path)
            documents.extend(loader.load())
    return documents

def main(args):
  documents_path = args[0]
  
  client = chromadb.HttpClient(settings=Settings(allow_reset=True))
  client.reset()
  collection = client.create_collection("pdfs")

  docs = get_documents(documents_path)
  
  for doc in docs:
    print('Storing:', doc.metadata['source']) 
    collection.add(
        ids=[str(uuid.uuid1())], metadatas=doc.metadata, documents=doc.page_content
    )

if __name__ == "__main__":
    main(sys.argv[1:])