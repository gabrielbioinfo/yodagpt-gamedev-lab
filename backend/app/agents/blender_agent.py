import os

from app.memory.sqlite_memory import SQLiteChatHistory
from app.rag.faiss_store import load_faiss
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.chains import RetrievalQA
from langchain.memory import ConversationBufferMemory
from langchain_ollama import OllamaLLM

# LLM local via Ollama
llm = OllamaLLM(model="deepseek-r1:7b", base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"))

# Carrega os vetores FAISS
retriever = load_faiss().as_retriever(search_kwargs={"k": 5})

# Ferramenta para buscar nos docs do Blender
qa_tool = Tool(
    name="search_docs",
    func=RetrievalQA.from_chain_type(llm=llm, retriever=retriever).run,
    description="Use para responder perguntas sobre Blender e Geometry Nodes.",
)


# Função de chat do agente BlenderGPT
def blender_agent_chat(question: str, session_id: str) -> str:
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        chat_memory=SQLiteChatHistory(session_id=session_id),
        handle_parsing_errors=True,
    )

    agent_executor = initialize_agent(
        tools=[qa_tool], llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True, memory=memory
    )

    return agent_executor.run(question)
