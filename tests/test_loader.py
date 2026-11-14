from app.document_loader import load_pdf

pdf_path = "data/01_employee_handbook_and_instructions.pdf"

documents = load_pdf(pdf_path)

print("Total pages extracted:", len(documents))

for document in documents:
    print("\nSource:", document["metadata"]["source"])
    print("Page:", document["metadata"]["page"])
    print("Text:", document["content"][:200])