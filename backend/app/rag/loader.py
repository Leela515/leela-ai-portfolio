from pathlib import Path
from backend.app.rag.models import KnowledgeDocument

class KnowledgeLoader:
    def __init__(self, knowledge_dir: str | Path):
        self.knowledge_dir = Path(knowledge_dir)

    def load_markdown_files(self) -> list[KnowledgeDocument]:
        if not self.knowledge_dir.exists():
            raise FileNotFoundError(f"Knowledge directory '{self.knowledge_dir}' does not exist.")
        
        documents: list[KnowledgeDocument] = []

        for file_path in sorted(self.knowledge_dir.rglob("*.md")):
            content = file_path.read_text(encoding="utf-8").strip()

            if not content:
                continue

            documents.append(
                KnowledgeDocument(
                    source=str(file_path),
                    content=content
                )
            )
        
        return documents