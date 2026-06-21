from backend.app.rag.answer_generator import AnswerGenerator
from backend.app.rag.retriever import Retriever
from backend.app.schemas.chat import ChatResponse, SourceResponse

INSUFFICIENT_CONTEXT_ANSWER = (
    "The available portfolio documents do not provide enough evidence to answer that confidently."
)

class PortfolioAssistantService:
    def __init__(
            self,
            retriever: Retriever,
            answer_generator: AnswerGenerator,
    ):
        self.retriever = retriever
        self.answer_generator = answer_generator

    def answer_question(self, question: str) -> ChatResponse:
        if not question.strip():
            raise ValueError("Question cannot be empty.")
        
        retrieved_chunks = self.retriever.retrieve(question, top_k=3)

        if not retrieved_chunks:
            return ChatResponse(
                question=question,
                answer=INSUFFICIENT_CONTEXT_ANSWER,
                sources=[],
            )
        
        generated = self.answer_generator.generate(
            question=question,
            retrieved_chunks=retrieved_chunks
        )

        return ChatResponse(
            question=question,
            answer=generated.answer,
            sources=[
                SourceResponse(
                    label=source.label,
                    title=source.title,
                    section=source.section,
                    document_type=source.document_type,
                    source=source.source,
                    chunk_id=source.chunk_id,
                )
                for source in generated.sources
            ],
        )