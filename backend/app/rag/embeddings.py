from sentence_transformers import SentenceTransformer

class EmbeddingModel:
    def __init__(self, model_name: str = "BAAI/bge-small-en-v1.5"):
        self.model = SentenceTransformer(model_name)

    def embed_text(self, text: str) -> list[float]:
        if not text.strip():
            raise ValueError("Text cannot be empty.")
        
        embedding = self.model.encode(text, normalize_embeddings=True)

        return embedding.tolist()
    
    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        if not texts:
            raise ValueError("Texts list cannot be empty.")
        
        if any(not text.strip() for text in texts):
            raise ValueError("Text list cannot contain empty text.")
        
        embeddings = self.model.encode(texts, normalize_embeddings=True)

        return embeddings.tolist()