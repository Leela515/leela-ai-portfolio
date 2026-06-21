from pathlib import Path
import yaml
from backend.app.rag.models import KnowledgeDocument

class KnowledgeLoader:
    def __init__(self, knowledge_dir: str | Path):
        self.knowledge_dir = Path(knowledge_dir)

    def load_markdown_files(self) -> list[KnowledgeDocument]:
        if not self.knowledge_dir.exists():
            raise FileNotFoundError(f"Knowledge directory '{self.knowledge_dir}' does not exist.")
        
        documents: list[KnowledgeDocument] = []

        for file_path in sorted(self.knowledge_dir.rglob("*.md")):
            raw_content = file_path.read_text(encoding="utf-8").strip()

            if not raw_content:
                continue

            metadata, content = self._parse_frontmatter(raw_content)

            documents.append(
                KnowledgeDocument(
                    source=str(file_path),
                    content=content,
                    document_type=metadata.get("document_type", "general"),
                    title=metadata.get("title", file_path.stem)
                )
            )
        
        return documents
    
    def _parse_frontmatter(self, raw_content: str) -> tuple[dict, str]:
        if not raw_content.startswith("---"):
            return {}, raw_content
        
        parts = raw_content.split("---", 2)

        if len(parts) < 3:
            return {}, raw_content
        
        metadata_text = parts[1].strip()
        content = parts[2].strip()

        metadata = yaml.safe_load(metadata_text) or {}

        return metadata, content
        