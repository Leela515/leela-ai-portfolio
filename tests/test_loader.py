from pathlib import Path
import pytest
from backend.app.rag.loader import KnowledgeLoader, KnowledgeDocument

def test_load_markdown_files_loads_valid_documents(tmp_path: Path):
    knowledge_dir = tmp_path / "knowledge"
    knowledge_dir.mkdir()

    profile_file = knowledge_dir / "profile.md"
    profile_file.write_text("# Leela Profile\nApplied AI/ML Engineer", encoding="utf-8")

    loader = KnowledgeLoader(knowledge_dir)
    documents = loader.load_markdown_files()

    assert len(documents) == 1
    assert documents[0].source.endswith("profile.md")
    assert "Applied AI/ML Engineer" in documents[0].content

def test_load_markdown_files_skips_empty_documents(tmp_path: Path):
    knowledge_dir = tmp_path / "knowledge"
    knowledge_dir.mkdir()

    empty_file = knowledge_dir / "empty.md"
    empty_file.write_text(" ", encoding="utf-8")

    loader = KnowledgeLoader(knowledge_dir)
    documents = loader.load_markdown_files()

    assert documents == []

def test_load_markdown_files_raises_error_for_missing_directory(tmp_path: Path):
    missing_dir = tmp_path / "missing"

    loader = KnowledgeLoader(missing_dir)

    with pytest.raises(FileNotFoundError):
        loader.load_markdown_files()