import pytest

from backend.app.rag.answer_generator import GeneratedAnswer, SourceReference
from backend.app.rag.models import DocumentChunk, RetrievedChunk
from backend.app.services.portfolio_assistant_service import (
    INSUFFICIENT_CONTEXT_ANSWER,
    PortfolioAssistantService,
)

class FakeRetriever:
    def __init__(self, results):
        self.results = results

    def retrieve(self, question: str, top_k: int = 3):
        return self.results

class FakeRetriever:
    def __init__(self, results):
        self.results = results

    def retrieve(self, question: str, top_k: int = 3):
        return self.results


class FakeAnswerGenerator:
    def generate(self, question: str, retrieved_chunks):
        return GeneratedAnswer(
            answer="Leela used PyTorch and RTMPose. [Source 1]",
            sources=[
                SourceReference(
                    label="Source 1",
                    title="Underwater Swimmer Pose Estimation",
                    section="Technology Stack",
                    document_type="project",
                    source="underwater.md",
                    chunk_id="chunk-1",
                )
            ],
        )
    
def test_service_returns_answer_with_sources():
    chunk = DocumentChunk(
        source="underwater.md",
        section="Technology Stack",
        content="PyTorch and RTMPose were used.",
        chunk_id="chunk-1",
        document_type="project",
        title="Underwater Swimmer Pose Estimation",
    )

    retrieved_chunk = RetrievedChunk(chunk=chunk, score=8.0)

    service = PortfolioAssistantService(
        retriever=FakeRetriever([retrieved_chunk]),
        answer_generator=FakeAnswerGenerator(),
    )

    response = service.answer_question("What technologies were used?")

    assert response.question == "What technologies were used?"
    assert "PyTorch" in response.answer
    assert len(response.sources) == 1
    assert response.sources[0].label == "Source 1"


def test_service_returns_insufficient_context_when_no_chunks():
    service = PortfolioAssistantService(
        retriever=FakeRetriever([]),
        answer_generator=FakeAnswerGenerator(),
    )

    response = service.answer_question("Unrelated question")

    assert response.answer == INSUFFICIENT_CONTEXT_ANSWER
    assert response.sources == []


def test_service_raises_error_for_empty_question():
    service = PortfolioAssistantService(
        retriever=FakeRetriever([]),
        answer_generator=FakeAnswerGenerator(),
    )

    with pytest.raises(ValueError):
        service.answer_question("   ")