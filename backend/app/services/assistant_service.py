from backend.app.schemas.chat import ChatRequest, ChatResponse

class AssistantService:
    def answer_question(self, request: ChatRequest) -> ChatResponse:
        return ChatResponse(
            answer="This is a placeholder answer for: {request.question}",
            sources=[]
        )