import os

from sqlmodel import Session, create_engine

DB_FILE = "data/yodagpt.db"
os.makedirs("data", exist_ok=True)

sqlite_url = f"sqlite:///{DB_FILE}"
engine = create_engine(sqlite_url, echo=False)


def get_session():
    return Session(engine)
