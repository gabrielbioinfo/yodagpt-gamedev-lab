from app.db.models import ChatMemory
from app.db.session import get_session
from fastapi import APIRouter
from sqlmodel import select

router = APIRouter(prefix="/history", tags=["Chat History"])


@router.get("/{session_id}")
def get_history(session_id: str):
    with get_session() as session:
        result = session.exec(
            select(ChatMemory).where(ChatMemory.session_id == session_id).order_by(ChatMemory.created_at)
        ).all()

        return [{"role": msg.role, "content": msg.content, "created_at": msg.created_at.isoformat()} for msg in result]


@router.delete("/{session_id}")
def clear_history(session_id: str):
    with get_session() as session:
        session.exec(f"DELETE FROM chat_memory WHERE session_id = :sid", {"sid": session_id})
        session.commit()
    return {"status": "cleared", "session_id": session_id}
