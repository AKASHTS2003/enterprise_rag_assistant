import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env")

client = genai.Client(api_key=api_key)


def embed_chunks(chunks, batch_size=50):
    """
    Convert text chunks into numerical embeddings.
    """

    all_embeddings = []

    for start in range(0, len(chunks), batch_size):
        batch = chunks[start:start + batch_size]

        texts = [chunk["content"] for chunk in batch]

        response = client.models.embed_content(
            model="gemini-embedding-001",
            contents=texts,
            config=types.EmbedContentConfig(
                task_type="RETRIEVAL_DOCUMENT"
            )
        )

        for chunk, embedding in zip(batch, response.embeddings):
            all_embeddings.append({
                "content": chunk["content"],
                "metadata": chunk["metadata"],
                "embedding": embedding.values
            })

    return all_embeddings

def embed_query(question):
    """
    Convert an employee question into an embedding.
    """

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=question,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_QUERY"
        )
    )

    return response.embeddings[0].values