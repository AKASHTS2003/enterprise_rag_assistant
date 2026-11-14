from pathlib import Path
from pypdf import PdfReader


def load_pdf(file_path):
    pdf_path = Path(file_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    reader = PdfReader(str(pdf_path))
    documents = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        if text.strip():
            documents.append({
                "content": text.strip(),
                "metadata": {
                    "source": pdf_path.name,
                    "page": page_number
                }
            })

    return documents


def load_all_pdfs(folder_path="data"):
    folder = Path(folder_path)

    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder}")

    all_documents = []

    pdf_files = sorted(folder.glob("*.pdf"))

    if not pdf_files:
        raise ValueError("No PDF files found in the data folder.")

    for pdf_file in pdf_files:
        documents = load_pdf(pdf_file)
        all_documents.extend(documents)

        print(f"Loaded: {pdf_file.name} | Pages: {len(documents)}")

    return all_documents