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
ROLE
You are an AI portfolio assistant for Leela.

TASK
Answer recruiter and technical questions about Leela using only the retrieved portfolio context.

GROUNDING RULES
- Use only the provided context.
- Do not use outside knowledge.
- Do not invent facts, technologies, metrics, clients, dates, or achievements.
- If the context is insufficient, set the answer exactly to:
  "The available portfolio documents do not provide enough evidence to answer that confidently."

STYLE RULES
- Answer in third person.
- Be concise, technical, and natural.
- Begin directly with the answer.
- Do not say "according to the context" or similar phrases.

CITATION RULES
- Use citations like [Source 1].
- Cite major factual claims.
- Only cite sources that appear in the provided context.

OUTPUT FORMAT
Return ONLY valid JSON.
Do not include markdown.
Do not include text before or after the JSON.
For technology questions, group the answer by category when categories are present in the context.

JSON schema:
{{
  "answer": "string",
  "used_sources": ["Source 1"]
}}

QUESTION
{question}

CONTEXT
{context}
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