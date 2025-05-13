from app.ingest.ingest_godot import ingest_godot_docs
from fastapi import APIRouter

router = APIRouter()


@router.post("/ingest/godot")
def ingest_godot():
    ingest_godot_docs()
    return {"status": "success", "message": "Documentação da Godot ingerida com sucesso"}
