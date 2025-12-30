from mcp_server.client import agent_instance 
import asyncio



if __name__ == "__main__":
	try:
		chosen = input("Choose provider (ollama/openai): ")
		user_prompt = input("Enter your prompt: ")
		response = asyncio.run(agent_instance(chosen, user_prompt))
	except ValueError as err:
		print(err)
		raise SystemExit(1)


	

    