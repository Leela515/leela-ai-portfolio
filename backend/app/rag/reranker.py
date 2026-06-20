from sentence_transformers import CrossEncoder

from backend.app.rag.models import RetrievedChunk


class CrossEncoderReranker:
    def __init__(self, model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"):
        self.model = CrossEncoder(model_name)

    def rerank(
        self,
        query: str,
        results: list[RetrievedChunk],
        top_k: int = 3,
    ) -> list[RetrievedChunk]:
        if not results:
            return []

        pairs = [
            (
                query,
                f"Section: {result.chunk.section}\n\nContent:\n{result.chunk.content}",
            )
            for result in results
        ]

        scores = self.model.predict(pairs)

        reranked = [
            RetrievedChunk(
                chunk=result.chunk,
                score=float(score),
            )
            for result, score in zip(results, scores)
        ]

        reranked.sort(key=lambda item: item.score, reverse=True)

        return reranked[:top_k]