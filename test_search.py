0
from app.search import search_documents

questions = [
    "What is the company office in Japan?",
    "What is my basic salary and what deductions apply?"
]

for question in questions:

    print("\n" + "=" * 70)
    print("QUESTION:", question)
    print("=" * 70)

    results = search_documents(question, top_k=5)

    for i, document in enumerate(results["documents"][0]):

        metadata = results["metadatas"][0][i]
        distance = results["distances"][0][i]

        print(f"\nResult {i + 1}")
        print("File:", metadata["source"])
        print("Page:", metadata["page"])
        print("Distance:", distance)
        print("Content:")
        print(document)