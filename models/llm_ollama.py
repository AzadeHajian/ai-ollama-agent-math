#Instantiation

from langchain_ollama import ChatOllama


def llm_instance(model="gemma:2b", temperature=0, timeout=300):
    """Create and return a ChatOpenAI instance with custom parameters."""
    llm = ChatOllama(
        model=model,
        temperature=temperature,
        timeout=timeout,
    )
    return llm









