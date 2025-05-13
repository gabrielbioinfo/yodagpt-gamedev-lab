import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

import os
from datetime import datetime

from app.db.models import Agent
from app.db.session import engine
from sqlmodel import Session


def register_agents():
    agents = [
        Agent(
            name="godotgpt",
            description="Especialista em Godot Engine 4.0, GDScript, nodes, cenas, debug...",
            model="deepseek-r1:7b",
            tools="search_docs",
            created_at=datetime.utcnow(),
        ),
        Agent(
            name="shadergpt",
            description="Ajuda com shaders, visual FX, material graph, e matemática gráfica",
            model="deepseek-r1:7b",
            tools="search_docs",
            created_at=datetime.utcnow(),
        ),
        Agent(
            name="blendergpt",
            description="Especialista em Blender, com foco em Geometry Nodes e sistemas visuais.",
            model="deepseek-r1:7b",
            tools="search_docs",
            created_at=datetime.utcnow(),
        ),
    ]

    with Session(engine) as session:
        for agent in agents:
            existing = session.get(Agent, agent.name)
            if not existing:
                session.add(agent)
                print(f"✅ Registrado: {agent.name}")
            else:
                print(f"ℹ️ Já existe: {agent.name}")
        session.commit()


if __name__ == "__main__":
    register_agents()
