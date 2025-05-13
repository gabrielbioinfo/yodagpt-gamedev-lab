from typing import List
from langchain.schema import BaseMessage, HumanMessage, AIMessage
from langchain.memory.chat_memory import BaseChatMessageHistory
from app.memory.db_memory import load_messages, save_message


class PostgresChatHistory(BaseChatMessageHistory):
    def __init__(self, session_id: str):
        self.session_id = session_id

    @property
    def messages(self) -> List[BaseMessage]:
        history = load_messages(self.session_id)
        return [
            HumanMessage(content=msg) if role == "user" else AIMessage(content=msg)
            for role, msg in history
        ]

    def add_user_message(self, message: str) -> None:
        save_message(self.session_id, "user", message)

    def add_ai_message(self, message: str) -> None:
        save_message(self.session_id, "ai", message)

    def clear(self) -> None:
        # Opcional: para apagar histórico se necessário
        pass
