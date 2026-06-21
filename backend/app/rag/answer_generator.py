from dataclasses import dataclass
from backend.app.llm.base import BaseLLM
from backend.app.rag.models import RetrievedChunk
from backend.app.rag.prompt_builder import PromptBuilder

@dataclass(frozen=True)
class SourceReference:
    label: str
    title: str
    section: str
    document_type: str
    source: str
    chunk_id: str

@dataclass(frozen=True)
class GeneratedAnswer:
    answer: str
    sources: list[SourceReference]

class AnswerGenerator:
    def __init__(
        self,
        llm: BaseLLM,
        prompt_builder: PromptBuilder,
    ):
        self.llm = llm
        self.prompt_builder = prompt_builder

    def generate(
        self,
        question: str,
        retrieved_chunks: list[RetrievedChunk],
    ) -> GeneratedAnswer:
        prompt = self.prompt_builder.build_prompt(
            question=question,
            retrieved_chunks=retrieved_chunks,
        )

        answer = self.llm.generate(prompt)

        sources = self._build_sources(retrieved_chunks)

        return GeneratedAnswer(
            answer=answer,
            sources=sources,
        )
    
    def _build_sources(
        self,
        retrieved_chunks: list[RetrievedChunk],
    ) -> list[SourceReference]:
        sources: list[SourceReference] = []

        for index, result in enumerate(retrieved_chunks, start=1):
            chunk = result.chunk
            
            sources.append(
                SourceReference(
                    label=f"Source {index}",
                    title=chunk.title,
                    section=chunk.section,
                    document_type=chunk.document_type,
                    source=chunk.source,
                    chunk_id=chunk.chunk_id,
                )
            )
        return sources