from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Agent(SQLModel, table=True):
    name: str = Field(primary_key=True)
    description: Optional[str] = None
    model: str
    tools: Optional[str] = Field(default=None, description="Lista separada por vírgula: 'tool1,tool2'")
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Session(SQLModel, table=True):
    id: str = Field(primary_key=True)
    agent_name: str = Field(foreign_key="agent.name")
    title: str = Field(default="Nova conversa")
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ChatMemory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    session_id: str = Field(foreign_key="session.id")
    role: str
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
