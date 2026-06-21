import pytest
from backend.app.rag.models import DocumentChunk
from backend.app.rag.retriever import Retriever
from backend.app.rag.vector_store import VectorStore

class FakeEmbeddingModel:
    def embed_text(self, text: str) -> list[float]:
        if "underwater" in text.lower():
            return [1.0, 0.0, 0.0]
        return [0.0, 1.0, 0.0]
    
def test_retriever_returns_relevant_chunks():
    vector_store = VectorStore(dimension=3)

    chunks = [
        DocumentChunk(
            source="underwater_pose_estimation.md",
            section="Technology Stack",
            content="RTMDet and RTMPose were used.",
            chunk_id="underwater-1",
            document_type="project",
            title="Test Project",
        ),
        DocumentChunk(
            source="ai_research_assistant.md",
            section="Technology Stack",
            content="FAISS and sentence-transformers were used.",
            chunk_id="rag-1",
            document_type="project",
            title="Test Project",
        ),
    ]

    embeddings = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
    ]

    vector_store.add_chunks(chunks, embeddings)

    retriever = Retriever(
        embedding_model=FakeEmbeddingModel(),
        vector_store=vector_store,
    )

    results = retriever.retrieve(
        "What technologies were used in the underwater project?",
        top_k=1,
    )

    assert len(results) == 1
    assert results[0].chunk.chunk_id == "underwater-1"
    assert results[0].score == pytest.approx(1.0)

def test_retriever_raises_error_for_empty_query():
    vector_store = VectorStore(dimension=3)

    retriever = Retriever(
        embedding_model=FakeEmbeddingModel(),
        vector_store=vector_store,
    )

    with pytest.raises(ValueError):
        retriever.retrieve("  ")