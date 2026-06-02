from fastapi import APIRouter
from backend.app.services.assistant_service import AssistantService
from backend.app.schemas.chat import ChatRequest, ChatResponse

router = APIRouter()
assistant_service = AssistantService()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return assistant_service.answer_question(request)