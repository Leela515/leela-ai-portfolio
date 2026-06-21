from pydantic import BaseModel

class ChatRequest(BaseModel):
    question: str

class SourceResponse(BaseModel):
    label: str
    title: str
    section: str
    document_type: str
    source: str
    chunk_id: str

class ChatResponse(BaseModel):
    question: str
    answer: str
    sources: list[SourceResponse] = []