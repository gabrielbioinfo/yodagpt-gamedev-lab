from app.db.models import Agent, ChatMemory, Session
from app.db.session import engine
from sqlmodel import SQLModel


def setup_db():
    SQLModel.metadata.create_all(engine)
    print("✅ Tabelas criadas com sucesso no SQLite!")


if __name__ == "__main__":
    setup_db()
