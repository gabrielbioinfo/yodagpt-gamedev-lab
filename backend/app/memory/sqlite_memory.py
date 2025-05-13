from typing import List

from app.db.models import ChatMemory
from app.db.session import get_session
from langchain.memory.chat_memory import BaseChatMessageHistory
from langchain.schema import AIMessage, BaseMessage, HumanMessage
from sqlmodel import select


class SQLiteChatHistory(BaseChatMessageHistory):
    def __init__(self, session_id: str):
        self.session_id = session_id

    @property
    def messages(self) -> List[BaseMessage]:
        with get_session() as session:
            result = session.exec(
                select(ChatMemory).where(ChatMemory.session_id == self.session_id).order_by(ChatMemory.created_at)
            )
            return [
                HumanMessage(content=msg.content) if msg.role == "user" else AIMessage(content=msg.content)
                for msg in result
            ]

    def add_user_message(self, message: str) -> None:
        with get_session() as session:
            msg = ChatMemory(session_id=self.session_id, role="user", content=message)
            session.add(msg)
            session.commit()

    def add_ai_message(self, message: str) -> None:
        with get_session() as session:
            msg = ChatMemory(session_id=self.session_id, role="ai", content=message)
            session.add(msg)
            session.commit()

    def clear(self) -> None:
        with get_session() as session:
            session.exec(select(ChatMemory).where(ChatMemory.session_id == self.session_id).delete())
            session.commit()
