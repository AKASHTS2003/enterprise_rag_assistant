from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load the API key from .env
load_dotenv()

# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0.2
)

# Send a test question
response = llm.invoke(
    "Explain Retrieval-Augmented Generation in simple words."
)

# Display the response
print(response.content)