import os
from dotenv import load_dotenv
from google import genai

from app.search import search_documents

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def answer_question(question):
    """
    Retrieve relevant documents and generate
    an answer grounded in their content.
    """

    # Step 1: Retrieve relevant chunks
    results = search_documents(question, top_k=5)

    if not results["documents"] or not results["documents"][0]:
        return {"answer": "I could not find relevant information.", "sources": []}

    # Step 2: Prepare context for Gemini
    context_parts = []
    sources = []
    seen_sources = set()

    for i, document in enumerate(results["documents"][0]):
        metadata = results["metadatas"][0][i]

        source_key = (metadata["source"], metadata["page"])

        if source_key not in seen_sources:
            seen_sources.add(source_key)

            sources.append({"file": metadata["source"], "page": metadata["page"]})

        context_parts.append(
            f"""
            Source: {metadata["source"]}
            Page: {metadata["page"]}
            Content: {document}
            """
        )

    context = "\n".join(context_parts)

    # Step 3: Create prompt
    prompt = f"""
        You are an accurate Enterprise Employee Knowledge Assistant.

        Your job is to answer employee questions using the
        provided document context.

        STRICT RULES:

        1. Use the information in the context to answer the question.
        2. If an exact amount, date, name, or policy is available,
            provide it directly.
        3. Never ignore relevant information that is explicitly
            present in the context.
        4. Do not replace an available answer with generic advice
            such as "check the HR portal".
        5. If the documents do not contain the requested information,
            say:
                "Insufficient information in the available employee documents."
        6. Never invent or assume missing information.
        7. Clearly distinguish fictional sample records from
            actual employee records.
        8. If a document identifies a particular employee, mention
            that employee's name when presenting their details.
        9. Include the source filename and page number.

        DOCUMENT CONTEXT:

        {context}

        EMPLOYEE QUESTION:

        {question}

        Now answer the question directly using the available evidence.
        """

    # Step 4: Generate answer using Gemini
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite", contents=prompt
    )

    return {"answer": response.text, "sources": sources}
