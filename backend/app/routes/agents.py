from app.db.models import Agent
from app.db.session import get_session
from fastapi import APIRouter
from sqlmodel import select

router = APIRouter(prefix="/agents", tags=["Agentes"])


@router.get("/")
def list_agents():
    with get_session() as session:
        result = session.exec(select(Agent)).all()
        return [
            {
                "name": agent.name,
                "description": agent.description,
                "model": agent.model,
                "tools": agent.tools,
                "created_at": agent.created_at,
            }
            for agent in result
        ]
