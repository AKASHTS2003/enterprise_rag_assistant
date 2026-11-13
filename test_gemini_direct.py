from dotenv import load_dotenv
from google import genai
from google.genai import errors
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env")

client = genai.Client(api_key=api_key)

models = [
    "gemini-3.1-flash-lite"
]

question = "Explain Retrieval-Augmented Generation in simple words."

for model in models:
    print(f"\n{'=' * 50}")
    print(f"Testing model: {model}")
    print('=' * 50)

    try:
        response = client.models.generate_content(
            model=model,
            contents=question
        )

        print("STATUS: SUCCESS")
        print("RESPONSE:")
        print(response.text)

    except errors.APIError as e:
        print("STATUS: FAILED")
        print("ERROR:", e)

print("\nAll model tests completed.")