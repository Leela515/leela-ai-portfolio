from backend.app.rag.embeddings import EmbeddingModel
from backend.app.rag.models import RetrievedChunk
from backend.app.rag.vector_store import VectorStore

class Retriever:
    def __init__(self, embedding_model: EmbeddingModel, vector_store: VectorStore):
        self.embedding_model = embedding_model
        self.vector_store = vector_store

    def retrieve(self, query: str, top_k: int = 3) -> list[RetrievedChunk]:
        if not query.strip():
            raise ValueError ("Query cannot be empty.")
        
        query_embedding = self.embedding_model.embed_text(query)
        results = self.vector_store.search(query_embedding, top_k=top_k)

        return [
            RetrievedChunk(chunk=chunk, score=score)
            for chunk, score in results
        ]