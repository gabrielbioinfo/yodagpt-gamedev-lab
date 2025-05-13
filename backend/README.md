# 🧠 YodaGPT GameDev Lab

Um laboratório local com IA para ajudar no desenvolvimento de jogos, usando RAG com FAISS, memória persistente com SQLite, e agentes especializados como o GodotGPT.

---

## ✅ Requisitos

- Python 3.11+
- [Ollama](https://ollama.com/) instalado e configurado
- Modelo `deepseek-r1:7b` já baixado:
  ```bash
  ollama pull deepseek-r1:7b
  ```

---

## 🛠️ Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/yodagpt-gamedev-lab.git
cd yodagpt-gamedev-lab

# Crie e ative o ambiente virtual
uv venv .venv
uv pip install -r requirements.txt
```

---

## 📂 Estrutura principal

```
scripts/         ← Scripts de automação (rodar app, setup, ingestão)
app/
  db/            ← Modelos SQLModel e conexão SQLite
  memory/        ← Memória LangChain persistente com SQLite
  agents/        ← Agentes (ex: GodotGPT)
  rag/           ← Vetor store (FAISS)
  ingest/        ← Ingestão de documentos da Godot
  routes/        ← Rotas FastAPI (chat, sessões, histórico)
```

---

## 🚀 Executando a aplicação

Use o script de tarefas:

```bash
uv run scripts/tasks.py
```

Você verá um menu com opções como:

- Criar banco de dados
- Rodar Ollama com GPU
- Rodar o backend
- Ingerir documentos da Godot

---

## 🌐 Endpoints principais (FastAPI)

- `POST /sessions` → cria nova sessão de chat
- `GET /sessions/{agent_name}` → lista sessões existentes
- `POST /chat/godotgpt` → envia mensagem para o agente com session_id
- `GET /history/{session_id}` → consulta o histórico de uma sessão
- `DELETE /history/{session_id}` → limpa a memória de uma sessão

---

## 📚 Documentação da Godot

É ingerida via `crawl4ai` e armazenada localmente com embeddings no FAISS.

---

## ✨ Em breve

- Registro dinâmico de agentes
- Interface frontend (Streamlit ou React)
- Indexação de cursos, vídeos e PDF

---

## 🧙 Feito com carinho e força da Força.
