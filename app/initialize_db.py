import streamlit as st

from app.document_loader import load_all_pdfs
from app.embeddings import embed_chunks
from app.text_splitter import create_chunks
from app.vector_store import save_embeddings


@st.cache_resource
def initialize_knowledge_base():
    """
    Load PDFs, generate embeddings and initialize ChromaDB.
    Runs once per application process.
    """

    # Step 1: Load all PDFs
    documents = load_all_pdfs("data")

    # Step 2: Split documents into chunks
    chunks = create_chunks(documents)

    # Step 3: Generate embeddings
    embedded_chunks = embed_chunks(chunks)

    # Step 4: Store embeddings in ChromaDB
    collection = save_embeddings(embedded_chunks)

    return collection