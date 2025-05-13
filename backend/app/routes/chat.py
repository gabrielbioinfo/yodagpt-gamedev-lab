from app.agents.blender_agent import blender_agent_chat
from app.agents.godot_agent import godot_agent_chat
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/chat", tags=["Chat"])


class ChatRequest(BaseModel):
    message: str
    session_id: str


AGENT_DISPATCH = {"godotgpt": godot_agent_chat, "blendergpt": blender_agent_chat}


@router.post("/{agent_name}")
def chat(agent_name: str, data: ChatRequest):
    agent = AGENT_DISPATCH.get(agent_name)
    if not agent:
        raise HTTPException(status_code=404, detail=f"Agente '{agent_name}' não encontrado.")

    response = agent(data.message, data.session_id)
    return {"response": response}
