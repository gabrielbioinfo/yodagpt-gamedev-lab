import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

import os

from app.rag.faiss_store import store_documents
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader

PDF_PATH = "data/blender/pdf/geometry_nodes_manual.pdf"


def ingest_blender_docs():
    print(f"📄 Lendo PDF: {PDF_PATH}")
    loader = PyMuPDFLoader(PDF_PATH)
    docs = loader.load()

    print(f"🧩 Dividindo {len(docs)} páginas em chunks...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    split_docs = splitter.split_documents(docs)

    print(f"🔢 Total de chunks: {len(split_docs)}")
    formatted_docs = [{"text": d.page_content, "source": d.metadata.get("source", "blender")} for d in split_docs]

    print("🧠 Armazenando no FAISS index...")
    store_documents(formatted_docs)
    print("✅ Ingestão finalizada.")


if __name__ == "__main__":
    ingest_blender_docs()
