import pytest
from backend.app.rag.models import DocumentChunk
from backend.app.rag.vector_store import VectorStore

def test_vector_store_adds_and_searches_chunks():
    store = VectorStore(dimension=3)

    chunks = [
        DocumentChunk(
            source="profile.md",
            section="Profile",
            content="Leela is an Applied AI/ML Engineer.",
            chunk_id="profile-1",
            document_type="project",
            title="Test Project",
        ),
        DocumentChunk(
            source="project.md",
            section="RAG",
            content="the project uses retrieval augmented generation.",
            chunk_id="project-1",
            document_type="project",
            title="Test Project",
        ),
    ]

    embeddings = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
    ]

    store.add_chunks(chunks, embeddings)

    results = store.search([1.0, 0.0, 0.0], top_k=1)

    assert len(results) == 1
    assert results[0][0].chunk_id == "profile-1"
    assert results[0][1] == pytest.approx(1.0)

def test_vector_store_returns_empty_when_no_chunks_exist():
    store = VectorStore(dimension=3)

    results = store.search([1.0, 0.0, 0.0])

    assert results == []

def test_vector_store_raises_error_for_mismatched_chunks_and_embeddings():
    store = VectorStore(dimension=3)

    chunks = [
        DocumentChunk(
            source="profile.md",
            section="Profile",
            content="Leela profile",
            chunk_id="profile-1",
            document_type="project",
            title="Test Project",
        )
    ]

    embeddings = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
    ]

    with pytest.raises(ValueError):
        store.add_chunks(chunks, embeddings)


def test_vector_store_raises_error_for_wrong_embedding_dimension():
    store = VectorStore(dimension=3)

    chunks = [
        DocumentChunk(
            source="profile.md",
            section="Profile",
            content="Leela profile",
            chunk_id="profile-1",
            document_type="project",
            title="Test Project",
        )
    ]

    embeddings = [[1.0, 0.0]]

    with pytest.raises(ValueError):
        store.add_chunks(chunks, embeddings)


def test_vector_store_raises_error_for_invalid_top_k():
    store = VectorStore(dimension=3)

    with pytest.raises(ValueError):
        store.search([1.0, 0.0, 0.0], top_k=0)