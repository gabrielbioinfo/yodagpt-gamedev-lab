import os
import subprocess
import sys
from pathlib import Path

# Adiciona a raiz do projeto ao sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from app.db.models import Agent, ChatMemory, Session, SQLModel
from app.db.session import engine

# from app.ingest.ingest_godot import ingest_godot_docs
from app.ingest.ingest_godot import ingest_godot_docs
from sqlmodel import SQLModel

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)


def create_db():
    print("✅ Criando tabelas...")
    SQLModel.metadata.create_all(engine)
    print("🧠 Banco de dados criado em data/yodagpt.db")


def setup_db_script():
    SQLModel.metadata.create_all(engine)
    print("✅ Tabelas criadas com sucesso no SQLite!")


def run_backend():
    print("🚀 Iniciando backend FastAPI...")
    subprocess.run(["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"])


def start_ollama():
    print("⚙️ Iniciando servidor Ollama com GPU (32 layers)...")
    subprocess.Popen(
        ["cmd", "/c", "set OLLAMA_NUM_GPU_LAYERS=32 && ollama serve"], creationflags=subprocess.CREATE_NEW_CONSOLE
    )


def ingest_godot():
    print("📥 Ingerindo documentos da Godot...")
    ingest_godot_docs()
    ingest_godot_docs()


def show_menu():
    print("\nYodaGPT GameDev Lab - Tarefas disponíveis:")
    print("1 - Criar banco de dados (SQLite)")
    print("2 - Setup do banco de dados (SQLite)")
    print("3 - Iniciar Ollama com GPU")
    print("4 - Iniciar backend FastAPI")
    print("5 - Ingerir documentação da Godot")
    print("0 - Sair\n")


if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Escolha a opção: ").strip()

        if choice == "1":
            create_db()
        elif choice == "2":
            setup_db_script()
        elif choice == "3":
            start_ollama()
        elif choice == "4":
            run_backend()
        elif choice == "5":
            ingest_godot()
        elif choice == "0" or choice == "x":
            print("👋 Encerrando script.")
            sys.exit(0)
        else:
            print("Opção inválida.\n")
