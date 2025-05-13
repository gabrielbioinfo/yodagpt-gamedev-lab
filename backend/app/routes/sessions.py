from app.memory.session_manager import create_session, list_sessions
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/sessions", tags=["Sessions"])


class SessionCreateRequest(BaseModel):
    agent_name: str
    title: str = "Nova conversa"


@router.post("/")
def create_new_session(payload: SessionCreateRequest):
    session_id = create_session(payload.agent_name, payload.title)
    return {"session_id": session_id}


@router.get("/{agent_name}")
def get_sessions_for_agent(agent_name: str):
    sessions = list_sessions(agent_name=agent_name)
    return [
        {"session_id": s.id, "agent_name": s.agent_name, "title": s.title, "created_at": s.created_at.isoformat()}
        for s in sessions
    ]


@router.get("/")
def get_sessions():
    sessions = list_sessions(agent_name="all")
    return [
        {"session_id": s.id, "agent_name": s.agent_name, "title": s.title, "created_at": s.created_at.isoformat()}
        for s in sessions
    ]
