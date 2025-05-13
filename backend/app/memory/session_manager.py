import uuid
from datetime import datetime

from app.db.models import Session
from app.db.session import get_session
from sqlmodel import select


def create_session(agent_name: str, title: str = "Nova conversa") -> str:
    session_id = str(uuid.uuid4())

    new_session = Session(id=session_id, agent_name=agent_name, title=title, created_at=datetime.utcnow())

    with get_session() as session:
        session.add(new_session)
        session.commit()

    return session_id


def list_sessions(agent_name: str):
    with get_session() as session:
        if agent_name == "all":
            result = session.exec(select(Session).order_by(Session.created_at.desc())).all()
        else:
            result = session.exec(
                select(Session).where(Session.agent_name == agent_name).order_by(Session.created_at.desc())
            ).all()

        return result
