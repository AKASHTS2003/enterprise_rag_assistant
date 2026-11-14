import chromadb
from app.embeddings import embed_query


def search_documents(
    question,
    persist_directory="chroma_db",
    top_k=3
):
    """
    Search employee documents using semantic similarity.
    """

    client = chromadb.PersistentClient(
        path=persist_directory
    )

    collection = client.get_collection(
        name="employee_documents"
    )

    # Convert question into an embedding
    query_embedding = embed_query(question)

    # Search ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=min(top_k, collection.count()),
        include=["documents", "metadatas", "distances"]
    )

    return results