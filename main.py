from models.llm_ollama import llm_instance as llm_ollama
from models.llm_openai import llm_instance as llm_openai


def _build_llm(provider: str):
	provider = provider.strip().lower()
	if provider == "ollama":
		return llm_ollama()
	if provider == "openai":
		return llm_openai()
	raise ValueError("Provider must be 'ollama' or 'openai'.")


if __name__ == "__main__":
	try:
		chosen = input("Choose provider (ollama/openai): ")
		llm = _build_llm(chosen)
	except ValueError as err:
		print(err)
		raise SystemExit(1)

	user_prompt = input("Enter your prompt: ")
	# LangChain chat models expose invoke() for single-turn calls.
	result = llm.invoke(user_prompt)
	print(f"\nResponse from {chosen.strip().lower()}:\n{result.content}")
	

    