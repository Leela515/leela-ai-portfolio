import numpy as np
import faiss
from backend.app.rag.models import DocumentChunk

class VectorStore:
    def __init__(self, dimension: int = 384):
        self.dimension = dimension
        self.index = faiss.IndexFlatIP(dimension)
        self.chunks: list[DocumentChunk] = []

    def add_chunks(
        self,
        chunks: list[DocumentChunk],
        embeddings: list[list[float]],
    ) -> None:
        if len(chunks) != len(embeddings):
            raise ValueError("Number of chunks and embeddings must match.")
            
        vectors = np.array(embeddings, dtype="float32")

        if vectors.ndim != 2 or vectors.shape[1] != self.dimension:
            raise ValueError(
                f"Embeddings must have shape (n, {self.dimension})."
            )
            
        self.index.add(vectors)
        self.chunks.extend(chunks)

    def search(
            self,
            query_embedding: list[float],
            top_k: int = 3,
        ) -> list[tuple[DocumentChunk, float]]:
        if top_k <= 0:
            raise ValueError("top_k must be greater than 0.")
            
        if self.index.ntotal == 0:
            return []
            
        query_vector = np.array([query_embedding], dtype="float32")

        if query_vector.shape[1] != self.dimension:
            raise ValueError(
                f"Query embedding must have dimension {self.dimension}."
            )
            
        scores, indices = self.index.search(query_vector, top_k)

        results: list[tuple[DocumentChunk, float]] = []

        for score, index in zip(scores[0], indices[0]):
            if index == -1:
                continue

            results.append((self.chunks[index], float(score)))

        return results