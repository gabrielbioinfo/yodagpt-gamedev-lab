import os

from app.rag.faiss_store import load_faiss
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM

# ⚙️ LLM local via Ollama
llm = OllamaLLM(
    model="deepseek-r1:7b", base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")  # ou llama3, como preferir
)

# 🧠 Carrega o vetor store FAISS salvo localmente
retriever = load_faiss().as_retriever(search_kwargs={"k": 5})

# 🔁 Pipeline RAG: busca + resposta com contexto
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)


def godot_rag_query(question: str) -> str:
    result = qa_chain.run(question)
    return result
