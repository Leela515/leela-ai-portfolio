from pathlib import Path
from backend.app.rag.indexer import build_retriever

def test_build_retriever_from_markdown_documents(tmp_path: Path):
    knowledge_dir = tmp_path / "knowledge"
    knowledge_dir.mkdir()

    profile_file = knowledge_dir / "profile.md"
    profile_file.write_text(
        "# Profile\nLeela is an Applied AI/ML Engineer focused on RAG systems.",
        encoding="utf-8",
    )

    retriever = build_retriever(knowledge_dir)

    results = retriever.retrieve("What does Leela focus on?", top_k=1)

    assert len(results) == 1
    assert "RAG" in results[0].chunk.content