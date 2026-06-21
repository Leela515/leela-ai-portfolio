from backend.app.llm.base import BaseLLM
from backend.app.rag.answer_generator import AnswerGenerator
from backend.app.rag.models import DocumentChunk, RetrievedChunk
from backend.app.rag.prompt_builder import PromptBuilder


class FakeLLM(BaseLLM):
    def generate(self, prompt: str) -> str:
        return "Leela used PyTorch and RTMPose for the underwater pose estimation project. [Source 1]"


def test_answer_generator_returns_answer_and_sources():
    chunk = DocumentChunk(
        source="underwater.md",
        section="Technology Stack",
        content="The project used PyTorch and RTMPose.",
        chunk_id="chunk-1",
        document_type="project",
        title="Underwater Swimmer Pose Estimation",
    )

    retrieved_chunk = RetrievedChunk(chunk=chunk, score=8.2)

    generator = AnswerGenerator(
        llm=FakeLLM(),
        prompt_builder=PromptBuilder(),
    )

    result = generator.generate(
        question="What technologies were used?",
        retrieved_chunks=[retrieved_chunk],
    )

    assert "PyTorch" in result.answer
    assert len(result.sources) == 1
    assert result.sources[0].label == "Source 1"
    assert result.sources[0].title == "Underwater Swimmer Pose Estimation"
    assert result.sources[0].section == "Technology Stack"