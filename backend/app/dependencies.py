from fastapi import Request

from backend.app.llm.ollama_client import OllmaClient
from backend.app.rag.answer_generator import AnswerGenerator
from backend.app.rag.indexer import build_retriever
from backend.app.rag.prompt_builder import PromptBuilder
from backend.app.services.portfolio_assistant_service import PortfolioAssistantService

def create_protfolio_assistant_service() -> PortfolioAssistantService:
    retriever = build_retriever()

    llm = OllmaClient()

    answer_generator = AnswerGenerator(
        llm=llm,
        prompt_builder=PromptBuilder(),
    )

    return PortfolioAssistantService(
        retriever=retriever,
        answer_generator=answer_generator,
    )

def get_portfolio_assitant_service(
        request: Request,
) -> PortfolioAssistantService:
    return request.app.state.portfolio_assistant_service