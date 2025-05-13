import os

from langchain.docstore.document import Document
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

DB_DIR = "data"
DB_PATH = os.path.join(DB_DIR, "faiss_index")

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


def store_documents(docs: list[dict]):
    os.makedirs(DB_DIR, exist_ok=True)

    langchain_docs = [Document(page_content=d["text"], metadata={"source": d.get("source", "")}) for d in docs]
    db = FAISS.from_documents(langchain_docs, embedding_model)
    db.save_local(DB_PATH)


def load_faiss():
    return FAISS.load_local(DB_PATH, embedding_model, allow_dangerous_deserialization=True)
