# Enterprise AI Knowledge Assistant

An AI-powered Enterprise Knowledge Assistant that uses **Retrieval-Augmented Generation (RAG)** to answer questions from multiple company documents (PDFs). It combines Google's Gemini models, ChromaDB vector storage, and semantic search to retrieve relevant information and generate context-aware answers with source references.

The application allows users to interact with enterprise documents through a simple Streamlit interface, reducing the effort required to manually search through lengthy documents.

## 🚀 Live Demo

[Try the Enterprise AI Knowledge Assistant](https://enterpriseragassistant-fiywavkf9tq2fs8t4idsm9.streamlit.app/)

## ✨ Features

- **Multi-PDF Document Processing:** Loads and extracts text from multiple PDF documents.
- **Text Chunking:** Splits extracted content into smaller, overlapping chunks to improve retrieval.
- **Semantic Embeddings:** Uses Google's `gemini-embedding-001` model to convert text into vector embeddings.
- **Vector Database:** Stores document embeddings and metadata in ChromaDB.
- **Semantic Search:** Retrieves relevant document chunks based on the meaning of user questions.
- **AI-Powered Responses:** Uses Gemini `gemini-3.1-flash-lite` to generate answers based on retrieved context.
- **Source References:** Displays the source PDF and page number supporting the retrieved information.
- **Context-Grounded Answers:** Designed to answer using available document context rather than unsupported assumptions.
- **Interactive Interface:** Provides a Streamlit-based interface for asking questions and viewing responses.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| Google Gemini API | LLM-based answer generation |
| Gemini Embedding Model | Text embedding generation |
| ChromaDB | Vector database |
| PyPDF | PDF text extraction |

## 🧠 RAG Architecture

The application follows a Retrieval-Augmented Generation pipeline.

1. **Document Loading:** Reads multiple PDF files and extracts their text page by page.
2. **Text Chunking:** Divides extracted text into smaller chunks while preserving source and page metadata.
3. **Embedding Generation:** Converts document chunks into numerical vectors using Gemini embeddings.
4. **Vector Storage:** Stores embeddings, text chunks, and metadata in ChromaDB.
5. **Query Processing:** Converts the user's question into an embedding.
6. **Semantic Retrieval:** Searches ChromaDB for the most relevant document chunks.
7. **Answer Generation:** Sends the retrieved context and question to Gemini to generate a grounded response.
8. **Source Attribution:** Displays the document name and page number associated with the retrieved information.

## 📂 Project Structure

```text
enterprise-rag-assistant/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── document_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── search.py
│   ├── rag_chain.py
│   └── initialize_db.py
│
├── data/
│   ├── 01_employee_handbook_and_instructions.pdf
│   ├── 02_salary_and_payroll_policy.pdf
│   ├── 03_employee_offer_and_joining_instructions.pdf
│   └── 04_employee_directory_and_records.pdf
│
├── tests/
│   ├── __init__.py
│   └── test_rag.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/enterprise-rag-assistant.git
cd enterprise-rag-assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

Get an API key from [Google AI Studio](https://aistudio.google.com/apikey).

**Important:** Never commit your `.env` file or expose your API key publicly.

### 5. Run the application

```bash
python -m streamlit run app/main.py
```

The application will be available at:

```text
http://localhost:8501
```

## 💬 Example Questions

Users can ask questions based on the available enterprise documents, such as:

- When will I receive my monthly salary?
- What is the company's leave policy?
- What documents are required during employee onboarding?
- Where is the company's Japan office located?
- What are the employee working hours?

## 🔐 Security and Limitations

- The project uses fictional sample employee documents for demonstration.
- A valid Google Gemini API key is required.
- The application currently processes PDF documents available in the repository.
- Answer quality depends on the content and relevance of the retrieved documents.
- This project is a portfolio demonstration and should not be used to process confidential employee information without appropriate security controls.

## 🔮 Future Improvements

- Support uploading PDFs directly through the application.
- Add document-level filtering and more advanced retrieval strategies.
- Implement RAG evaluation using retrieval and answer-quality metrics.
- Add conversation memory for follow-up questions.
- Improve document processing and embedding efficiency.
- Introduce authentication and role-based document access.

## 👨‍💻 Author

**Akash T S**

- GitHub: [AKASHTS2003](https://github.com/AKASHTS2003)
- LinkedIn: [Connect on LinkedIn](https://www.linkedin.com/in/akash-t-shaju/)

---

⭐ If you find this project useful, consider giving the repository a star!
