import pytest

from backend.app.rag.models import DocumentChunk, RetrievedChunk
from backend.app.rag.prompt_builder import PromptBuilder


def test_prompt_builder_includes_question_and_context():
    chunk = DocumentChunk(
        source="underwater.md",
        section="Technology Stack",
        content="The project used PyTorch, OpenCV, RTMDet, and RTMPose.",
        chunk_id="chunk-1",
        document_type="project",
        title="Underwater Swimmer Pose Estimation",
    )

    retrieved = RetrievedChunk(chunk=chunk, score=8.5)

    builder = PromptBuilder()
    prompt = builder.build_prompt(
        question="What technologies were used?",
        retrieved_chunks=[retrieved],
    )

    assert "What technologies were used?" in prompt
    assert "[Source 1]" in prompt
    assert "Underwater Swimmer Pose Estimation" in prompt
    assert "Technology Stack" in prompt
    assert "PyTorch" in prompt

def test_prompt_builder_raises_error_for_empty_question():
    builder = PromptBuilder()

    with pytest.raises(ValueError):
        builder.build_prompt("   ", [])

def test_prompt_builder_handles_empty_context():
    builder = PromptBuilder()

    prompt = builder.build_prompt(
        question="What is Leela's focus area?",
        retrieved_chunks=[],
    )

    assert "No retrieved context was provided." in prompt
    assert "insufficient" in prompt.lower()