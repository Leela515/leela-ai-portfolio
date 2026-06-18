from dataclasses import dataclass

@dataclass(frozen=True)
class KnowledgeDocument:
    source: str
    content: str

@dataclass(frozen=True)
class DocumentChunk:
    source: str
    section: str
    content: str
    chunk_id: str

@dataclass(frozen=True)
class RetrievedChunk:
    chunk: DocumentChunk
    score: float