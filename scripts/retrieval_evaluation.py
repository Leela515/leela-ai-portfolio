from datetime import datetime
from pathlib import Path

from backend.app.rag.indexer import build_retriever


QUERIES = [
    "What technologies were used in the underwater project?",
    "What models were used in underwater swimmer pose estimation?",
    "Why was a two-stage pipeline used?",
    "What technologies were used in the AI Research Assistant?",
    "What was the main challenge of the spiking transformer?",
    "What roles is Leela targeting?",
    "What is Leela's focus area?",
]


def main() -> None:
    retriever = build_retriever()

    output_dir = Path("reports")
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / "retrieval_evaluation.md"

    lines: list[str] = []
    lines.append("# Retrieval Evaluation Report\n")
    lines.append(f"Generated at: {datetime.now().isoformat(timespec='seconds')}\n")

    for query in QUERIES:
        results = retriever.retrieve(query=query, top_k=3)

        lines.append("\n---\n")
        lines.append(f"## Query: {query}\n")

        for index, result in enumerate(results, start=1):
            lines.append(f"### Result {index}\n")
            lines.append(f"- Score: `{result.score:.4f}`")
            lines.append(f"- Source: `{result.chunk.source}`")
            lines.append(f"- Section: `{result.chunk.section}`")
            lines.append(f"- Chunk ID: `{result.chunk.chunk_id}`\n")

            lines.append("```text")
            lines.append(result.chunk.content[:800])
            lines.append("```\n")

    output_file.write_text("\n".join(lines), encoding="utf-8")

    print(f"Retrieval evaluation saved to: {output_file}")


if __name__ == "__main__":
    main()