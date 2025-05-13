import os

from app.memory.sqlite_memory import SQLiteChatHistory
from app.rag.faiss_store import load_faiss
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.chains import RetrievalQA
from langchain.memory import ConversationBufferMemory
from langchain_ollama import OllamaLLM

# LLM local via Ollama
llm = OllamaLLM(
    model=os.getenv("LLM_MODEL", "deepseek-r1:7b"), base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
)

# RAG com FAISS
retriever = load_faiss().as_retriever(search_kwargs={"k": 5})

# Ferramenta de busca nos docs da Godot
qa_tool = Tool(
    name="search_docs",
    func=RetrievalQA.from_chain_type(llm=llm, retriever=retriever).run,
    description="Use para responder perguntas relacionadas à documentação da Godot Engine.",
)


def godot_agent_chat(question: str, session_id: str) -> str:
    memory = ConversationBufferMemory(
        memory_key="chat_history", return_messages=True, chat_memory=SQLiteChatHistory(session_id=session_id)
    )

    agent_executor = initialize_agent(
        tools=[qa_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        memory=memory,
        handle_parsing_errors=True,
    )

    return agent_executor.run(question)
