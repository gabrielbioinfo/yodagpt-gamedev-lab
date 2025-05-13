# ========= CONFIG =========

DB_NAME = yodagpt
DB_USER = postgres
DB_HOST = localhost
DB_PORT = 5432
DB_URL = postgresql://$(DB_USER):$(DB_PASS)@$(DB_HOST):$(DB_PORT)/$(DB_NAME)

# ========= TASKS =========

.PHONY: help
help:
	@echo "YodaGPT GameDev Lab - Comandos úteis:"
	@echo "  make db-create      → Cria o banco $(DB_NAME)"
	@echo "  make db-tables      → Cria as tabelas (via vector_store.py)"
	@echo "  make ollama-run     → Inicia o servidor Ollama com GPU"
	@echo "  make run            → Roda o backend FastAPI com uvicorn"
	@echo "  make install        → Instala as dependências do projeto"

# ========= COMANDOS =========

db-create:
	@createdb -U $(DB_USER) $(DB_NAME)

db-tables:
	@echo "Criando tabelas no banco..."
	@uv run -c "from app.rag.vector_store import setup_tables; setup_tables()"
	@echo "Tabelas criadas com sucesso!"

ollama-run:
	@echo "Iniciando Ollama com GPU (layers=32)..."
	OLLAMA_NUM_GPU_LAYERS=32 ollama serve

run:
	@uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

install:
	@uv pip install -r requirements.txt
