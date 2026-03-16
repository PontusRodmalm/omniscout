import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env
# This ensures our API keys stay secret and safe.
load_dotenv()

def main():
    # Fetch the API key
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        print("❌ Error: GOOGLE_API_KEY not found in .env file.")
        print("Make sure you have a .env file with GOOGLE_API_KEY=your_key")
        return

    # Initialize the brain (The LLM)
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key
    )

    print("🤖 OmniScout is waking up...")
    
    query = "Introduce yourself in one short sentence as a professional research agent."
    
    try:
        # Calling the LLM
        response = llm.invoke(query)
        print(f"\nResponse: {response.content}")
        print("\n✅ Connection successful! OmniScout is online.")
    except Exception as e:
        print(f"\n❌ Something went wrong: {e}")

if __name__ == "__main__":
    main()