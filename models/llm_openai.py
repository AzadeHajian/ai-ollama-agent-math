import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

def __check_openai_api_key():
    "load and verify OpenAI API key from environment variable."
    load_dotenv()
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is not found.")
        return api_key
    except Exception as e: 
        print(f"Error loading OPENAI_API_KEY: {e}")
        return None
    

def llm_instance(model: str="gpt-3.5-turbo", temperature: int=0, timeout:int=300):
    """Create and return a ChatOpenAI instance with custom parameters."""
    __check_openai_api_key()
    llm = ChatOpenAI(
        model=model,
        temperature=temperature,
        timeout=timeout,
    )
    return llm
    

        

