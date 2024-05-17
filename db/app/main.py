import os
import fitz  # PyMuPDF
from chromadb import ChromaDB

def initialize_chromadb_with_pdfs(pdf_dir):
    # Initialize ChromaDB
    db = ChromaDB()

    # Process PDF files
    for pdf_file in os.listdir(pdf_dir):
        if pdf_file.endswith('.pdf'):
            pdf_path = os.path.join(pdf_dir, pdf_file)
            with fitz.open(pdf_path) as doc:
                text = ""
                for page in doc:
                    text += page.get_text()
                db.insert({"file_name": pdf_file, "content": text})

if __name__ == "__main__":
    pdf_directory = "/path/to/your/pdf/files"
    initialize_chromadb_with_pdfs(pdf_directory)
    print("PDF files have been processed and stored in ChromaDB")
