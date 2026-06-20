from backend.app.rag.indexer import build_retriever


def main():
    retriever = build_retriever()

    query = "What tools were used in underwater swimmer pose estimation?"

    results = retriever.retrieve(
        query=query,
        top_k=3,
    )

    print("\n" + "=" * 80)
    print(f"QUESTION: {query}")
    print("=" * 80)

    for index, result in enumerate(results, start=1):
        print(f"\nResult {index}")
        print("-" * 40)

        print(f"Score: {result.score:.4f}")
        print(f"Source: {result.chunk.source}")
        print(f"Section: {result.chunk.section}")

        print("\nContent:")
        print(result.chunk.content[:500])

        print("-" * 40)


if __name__ == "__main__":
    main()