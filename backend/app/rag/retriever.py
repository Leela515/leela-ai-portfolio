from backend.app.rag.embeddings import EmbeddingModel
from backend.app.rag.models import RetrievedChunk
from backend.app.rag.reranker import CrossEncoderReranker
from backend.app.rag.vector_store import VectorStore


class Retriever:
    def __init__(
        self,
        embedding_model: EmbeddingModel,
        vector_store: VectorStore,
        reranker: CrossEncoderReranker | None = None,
    ):
        self.embedding_model = embedding_model
        self.vector_store = vector_store
        self.reranker = reranker

    def retrieve(self, query: str, top_k: int = 3) -> list[RetrievedChunk]:
        if not query.strip():
            raise ValueError("Query cannot be empty.")

        query_embedding = self.embedding_model.embed_text(query)

        raw_results = self.vector_store.search(
            query_embedding=query_embedding,
            top_k=max(top_k, 10),
        )

        results = [
            RetrievedChunk(chunk=chunk, score=score)
            for chunk, score in raw_results
        ]

        if self.reranker:
            return self.reranker.rerank(
                query=query,
                results=results,
                top_k=top_k,
            )

        return results[:top_k]