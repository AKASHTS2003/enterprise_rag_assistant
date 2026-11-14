from app.document_loader import load_all_pdfs
from app.text_splitter import create_chunks
from app.embeddings import embed_chunks

# 1. Load all four PDFs
documents = load_all_pdfs("data")

# 2. Create text chunks
chunks = create_chunks(
    documents,
    chunk_size=500,
    overlap=100
)

print("\nTotal chunks:", len(chunks))

# 3. Generate embeddings
embedded_chunks = embed_chunks(chunks)

print("Total embeddings generated:", len(embedded_chunks))

# 4. Display the first embedding
if embedded_chunks:
    first = embedded_chunks[0]

    print("\nSource:", first["metadata"]["source"])
    print("Page:", first["metadata"]["page"])
    print("Embedding dimensions:", len(first["embedding"]))
    print("First 5 vector values:", first["embedding"][:5])