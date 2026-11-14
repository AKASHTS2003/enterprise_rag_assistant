from app.document_loader import load_all_pdfs
from app.text_splitter import create_chunks
from app.embeddings import embed_chunks
from app.vector_store import save_embeddings

# Step 1: Load all PDFs
documents = load_all_pdfs("data")

# Step 2: Create chunks
chunks = create_chunks(
    documents,
    chunk_size=500,
    overlap=100
)

print("\nTotal chunks:", len(chunks))

# Step 3: Generate embeddings
embedded_chunks = embed_chunks(chunks)

print("Total embeddings:", len(embedded_chunks))

# Step 4: Store in ChromaDB
collection = save_embeddings(embedded_chunks)

print("Database collection:", collection.name)
print("Total stored records:", collection.count())