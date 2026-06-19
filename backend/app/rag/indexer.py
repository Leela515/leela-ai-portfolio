from pathlib import Path
from backend.app.rag.chunker import MarkdownChunker
from backend.app.rag.embeddings import EmbeddingModel
from backend.app.rag.loader import KnowledgeLoader
from backend.app.rag.retriever import Retriever
from backend.app.rag.vector_store import VectorStore

def build_retriever(
        knowledge_dir: str | Path = "backend/app/knowledge/documents",
) -> Retriever:
    loader = KnowledgeLoader(knowledge_dir)
    documents = loader.load_markdown_files()

    chunker = MarkdownChunker()
    chunks = chunker.chunk_documents(documents)

    embedding_model = EmbeddingModel()
    embeddings = embedding_model.embed_texts(
        [chunk.content for chunk in chunks]
    )

    vector_store = VectorStore(dimension=384)
    vector_store.add_chunks(chunks, embeddings)

    return Retriever(
        embedding_model=embedding_model,
        vector_store=vector_store
    )