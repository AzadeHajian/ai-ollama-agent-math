from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from models.llm_ollama import llm_instance as llm_ollama
from models.llm_openai import llm_instance as llm_openai
import traceback
from prompts.prompt import general_prompt

def llm_select(llm_provider: str, model: str, temperature: float = 0, timeout: int = 300):
    provider = llm_provider.strip().lower()
    if provider == "ollama":
        return llm_ollama(model=model, temperature=temperature, timeout=timeout)
    if provider == "openai":
        return llm_openai(model=model, temperature=temperature, timeout=timeout)
    raise ValueError("Provider must be 'ollama' or 'openai'.")

async def agent_instance(llm_provider: str, model: str, user_prompt: str, temperature: float = 0, timeout: int = 300):
  
    # Define all tools in one MultiServerMCPClient config
    mcp_tools = MultiServerMCPClient(
        {
            "math": {  # name of the tool
                "command": "python",  # command to run the tool
                "args": ["tools/math_tool.py"],  # address of the tool
                "transport": "stdio",  # communication method which can be "stdio" or "remote"
            },
        }
    )
    print("Connecting to MCP tools and agents") # Initialize the MCP client

    # await is a part of async function to wait for the MCP client to be ready
    try:
        tools = await mcp_tools.get_tools()
    except Exception as e:
        print(f"Error getting tools from MCP client: {e}")
        traceback.print_exception(e)
        raise RuntimeError("Failed to get tools from MCP client.")
    
    print(f"Loaded Tools: {[tool.name for tool in tools]}")
    agent = create_react_agent(model=llm_select(llm_provider, model, temperature, timeout), tools=tools )  # Create the agent with the LLM and tools

    resposne = await agent.ainvoke(
        {
            "messages": [
                {"role": "system", "content":general_prompt()},
                {"role": "user", "content": user_prompt}
            ]
        }   
    )

    print("Agent response received")
    print(f"Agent Response: {resposne['messages'][-1].content}")
    return resposne["messages"][-1].content



