from app.ingest import ingest_router
from app.routes import agents as agents_routes
from app.routes import chat as chat_routes
from app.routes import history as history_routes
from app.routes import sessions as session_routes
from app.schemas.chat import ChatRequest
from fastapi import FastAPI

app = FastAPI(title="YodaGPT GameDev Lab")
app.include_router(ingest_router.router)
app.include_router(session_routes.router)
app.include_router(history_routes.router)
app.include_router(agents_routes.router)
app.include_router(chat_routes.router)


@app.get("/")
def root():
    return {"message": "YodaGPT GameDev Lab is up and running 🧠🎮"}
