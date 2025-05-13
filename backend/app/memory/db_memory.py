import os
from typing import List, Tuple
import psycopg2
from datetime import datetime

def get_connection():
    return psycopg2.connect(os.getenv("DATABASE_URL"))

def save_message(session_id: str, role: str, content: str):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO chat_memory (session_id, role, content, created_at)
                VALUES (%s, %s, %s, %s)
            """, (session_id, role, content, datetime.utcnow()))
        conn.commit()

def load_messages(session_id: str) -> List[Tuple[str, str]]:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT role, content FROM chat_memory
                WHERE session_id = %s
                ORDER BY created_at ASC
            """, (session_id,))
            return cur.fetchall()
