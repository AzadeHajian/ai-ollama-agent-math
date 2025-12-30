#Instantiation

from langchain_ollama import ChatOllama


def llm_instance(model , temperature, timeout):
    """Create and return a ChatOpenAI instance with custom parameters."""
    llm = ChatOllama(
        model=model,
        temperature=temperature,
        timeout=timeout,
    )
    return llm











