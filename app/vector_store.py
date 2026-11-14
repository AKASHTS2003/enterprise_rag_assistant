import hashlib
import chromadb


def save_embeddings(
    embedded_chunks,
    persist_directory="chroma_db"
):
    """
    Store text, embeddings and metadata in ChromaDB.
    """

    client = chromadb.PersistentClient(
        path=persist_directory
    )

    collection = client.get_or_create_collection(
        name="employee_documents",
        metadata={"hnsw:space": "cosine"}
    )

    ids = []
    documents = []
    metadatas = []
    embeddings = []

    for item in embedded_chunks:
        metadata = item["metadata"]

        unique_text = (
            f'{metadata["source"]}-'
            f'{metadata["page"]}-'
            f'{metadata["chunk"]}-'
            f'{item["content"]}'
        )

        document_id = hashlib.sha256(
            unique_text.encode("utf-8")
        ).hexdigest()

        ids.append(document_id)
        documents.append(item["content"])
        metadatas.append(metadata)
        embeddings.append(item["embedding"])

    if ids:
        collection.upsert(
            ids=ids,
            documents=documents,
            metadatas=metadatas,
            embeddings=embeddings
        )

    print("Total records stored:", collection.count())

    return collection