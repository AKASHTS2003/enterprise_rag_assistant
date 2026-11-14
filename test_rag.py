from app.rag_chain import answer_question

question = "When will I receive my monthly salary?"

result = answer_question(question)

print("\nEmployee Question:")
print(question)

print("\nAI Answer:")
print(result["answer"])

print("\nRetrieved Sources:")

for source in result["sources"]:
    print(
        "File:", source["file"],
        "| Page:", source["page"]
    )