from backend.app.rag.models import RetrievedChunk

class PromptBuilder:
    def build_prompt(
            self,
            question: str,
            retrieved_chunks: list[RetrievedChunk],
    ) -> str:
        
        if not question.strip():
            raise ValueError("Question cannot be empty.")
        
        context = self._format_context(retrieved_chunks)

        return f"""
You are an AI protfolio assistant for Leela.

Answer in the third person as an assistant.
Use a technical but concise tone.
Use only the provided context.
Do not use outside knowledge.
If the provided context is insufficient, say:
"The available portfolio documentsn do not provide enough evidence to answer that confidently."

Cite every factual claim using the format [Source 1], [Source 2], etc.
Do not invent citations.
Do not answer unrelated questions that are not supported by the portfolio context.

Question:
{question}

Context:
{context}

Answer:
""".strip()
    
    def _format_context(self, retrieved_chunks: list[RetrievedChunk]) -> str:
        if not retrieved_chunks:
            return "No retrieved context was provided."
        
        formatted_sources: list[str] = []

        for index, result in enumerate(retrieved_chunks, start=1):
            chunk = result.chunk
            
            formatted_sources.append(
                f"""
[Source {index}]
Title: {chunk.title}
Section: {chunk.section}
Document Type: {chunk.document_type}
Content:
{chunk.content}
""".strip()
            )

        return "\n\n".join(formatted_sources)