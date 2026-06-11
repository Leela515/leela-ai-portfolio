import re
from backend.app.rag.models import DocumentChunk, KnowledgeDocument

class MarkdownChunker:
    def chunk_documents(self, documents: list[KnowledgeDocument]) -> list[DocumentChunk]:
        chunks: list[DocumentChunk] = []

        for document in documents:
            chunks.extend(self.chunk_document(document))
        
        return chunks
    
    def chunk_document(self, document: KnowledgeDocument) -> list[DocumentChunk]:
        sections = self._split_by_markdown_headings(document.content)

        chunks: list[DocumentChunk] = []

        for index, section in enumerate(sections):
            section_title = section["title"]
            section_content = section["content"]

            if not section_content.strip():
                continue

            chunks.append(
                DocumentChunk(
                    source=document.source,
                    section=section_title,
                    content=section_content.strip(),
                    chunk_id=f"{document.source}::chunk-{index}"
                )
            )
        return chunks
    
    def _split_by_markdown_headings(self, content: str) -> list[dict[str, str]]:
        pattern = r"(?m)^#\s+(.+)$"
        matches = list(re.finditer(pattern, content))

        if not matches:
            return [{"title": "Document", "content": content.strip()}]
        
        sections: list[dict[str, str]] = []
        
        for index, match in enumerate(matches):
            title = match.group(1).strip()
            start = match.end()
            end = matches[index + 1].start() if index + 1 < len(matches) else len(content)

            section_content = content[start:end].strip()

            sections.append(
                {
                    "title": title,
                    "content": section_content,
                }
            )
        return sections