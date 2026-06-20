from backend.app.rag.models import DocumentChunk


class RetrievalTextBuilder:
    def build_text(self, chunk: DocumentChunk) -> str:
        return (
            f"Section: {chunk.section}\n\n"
            f"Content:\n{chunk.content}"
        )

    def build_texts(self, chunks: list[DocumentChunk]) -> list[str]:
        return [self.build_text(chunk) for chunk in chunks]