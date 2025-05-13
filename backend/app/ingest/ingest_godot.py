from app.rag.faiss_store import store_documents
from langchain_community.document_loaders import WebBaseLoader


def ingest_godot_docs():
    print("📥 Carregando página principal da Godot Docs...")
    loader = WebBaseLoader("https://docs.godotengine.org/en/stable/")
    documents = loader.load()

    print(f"🔢 {len(documents)} documentos carregados.")
    store_documents([{"text": doc.page_content, "source": doc.metadata.get("source", "")} for doc in documents])
    print("✅ Documentos indexados com sucesso no FAISS!")


if __name__ == "__main__":
    ingest_godot_docs()
