from backend.app.rag.chunker import MarkdownChunker
from backend.app.rag.models import KnowledgeDocument

def test_chunk_document_splits_markdown_by_headings():
    document = KnowledgeDocument(
        source="profile.md",
        content="# Overview\nLeela is an Applied AI/ML Engineer.\n\n# Skills\nRAG, LLMs, MLOps",
        document_type="profile",
        title="Test Profile",
    )

    chunker = MarkdownChunker()
    chunks = chunker.chunk_document(document)

    assert len(chunks) == 2
    assert chunks[0].section == "Overview"
    assert "Applied AI/ML Engineer" in chunks[0].content
    assert chunks[1].section == "Skills"
    assert "RAG" in chunks[1].content

def test_chunk_document_handles_document_without_headings():
    document = KnowledgeDocument(
        source="plain.md",
        content="This document has no markdown headings.",
        document_type="project",
        title="Test Project",
    )

    chunker = MarkdownChunker()
    chunks = chunker.chunk_document(document)

    assert len(chunks) == 1
    assert chunks[0].section == "Document"
    assert chunks[0].content == "This document has no markdown headings."

def test_chunk_documents_chunks_multiple_documents():
    documents = [
        KnowledgeDocument(
            source="one.md",
            content="# First\nContent of the first document.",
            document_type="project",
            title="Test Project",
        ),
        KnowledgeDocument(
            source="two.md",
            content="# Second\nContent of the second document.",
            document_type="project",
            title="Test Project",
        )
    ]

    chunker = MarkdownChunker()
    chunks = chunker.chunk_documents(documents)

    assert len(chunks) == 2
    assert chunks[0].source == "one.md"
    assert chunks[1].source == "two.md"