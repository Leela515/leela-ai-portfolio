import pytest
from backend.app.rag.embeddings import EmbeddingModel

def test_embed_text_returns_vector():
    model = EmbeddingModel()
    embedding = model.embed_text("Leela is an Applied AI/ML Engineer.")

    assert isinstance(embedding, list)
    assert len(embedding) == 384
    assert all(isinstance(value, float) for value in embedding)

def test_embed_texts_return_multiple_vectors():
    model = EmbeddingModel()
    embeddings = model.embed_texts([
        "Leela works on RAG systems.",
        "RTMDet was used for swimmer detection."
    ])

    assert len(embeddings) == 2
    assert len(embeddings[0]) == 384
    assert len(embeddings[1]) == 384

def test_embed_text_raises_error_for_empty_text():
    model = EmbeddingModel()

    with pytest.raises(ValueError):
        model.embed_text("   ")

def test_embed_texts_raises_error_for_empty_list():
    model = EmbeddingModel()

    with pytest.raises(ValueError):
        model.embed_texts([])