from app.document_loader import load_all_pdfs
from app.text_splitter import create_chunks

# Load all four PDF documents
documents = load_all_pdfs("data")

print("\nTotal PDF pages extracted:", len(documents))

# Create chunks from all extracted pages
chunks = create_chunks(
    documents,
    chunk_size=500,
    overlap=100
)

print("Total chunks created:", len(chunks))

# Display chunk information
for chunk in chunks:
    print("\nSource:", chunk["metadata"]["source"])
    print("Page:", chunk["metadata"]["page"])
    print("Chunk:", chunk["metadata"]["chunk"])
    print("Content:", chunk["content"][:200])