from dataclasses import dataclass

@dataclass(frozen=True)
class KnowledgeDocument:
    source: str
    content: str
    document_type: str
    title: str

@dataclass(frozen=True)
class DocumentChunk:
    source: str
    section: str
    content: str
    chunk_id: str
    document_type: str
    title: str

@dataclass(frozen=True)
class RetrievedChunk:
    chunk: DocumentChunk
    score: float