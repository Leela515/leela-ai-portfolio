from fastapi import APIRouter, Depends, HTTPException, status

from backend.app.llm.base import LLMGenerationError
from backend.app.dependencies import get_portfolio_assitant_service
from backend.app.services.portfolio_assistant_service import PortfolioAssistantService
from backend.app.schemas.chat import ChatRequest, ChatResponse
from backend.app.rag.answer_parser import AnswerParsingError
router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    service: PortfolioAssistantService = Depends(get_portfolio_assitant_service),
):
    try:
        return service.answer_question(request.question)
    except LLMGenerationError as error:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="LLM service unavailable."
        ) from error
    except AnswerParsingError as error:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="LLM returned an invalid structured response.",
        ) from error
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        ) from error