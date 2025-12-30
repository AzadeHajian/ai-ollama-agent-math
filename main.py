import streamlit as st
import asyncio
from mcp_server.client import agent_instance

# Page configuration
st.set_page_config(
    page_title="AI Math Agent",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 AI Math Agent")
st.markdown("Chat with an AI agent that can perform mathematical calculations")

# Sidebar for provider selection
with st.sidebar:
    st.header("⚙️ Settings")
    
    provider = st.selectbox(
        "Select LLM Provider",
        options=["ollama", "openai"],
        index=0
    )
    
    # Model selection based on provider
    if provider == "ollama":
        model = st.selectbox(
            "Select Model",
            options=["llama3.2:3b", "qwen2.5:3b", "gemma2:2b"],
            index=0,
            help="Note: Model must support tool calling"
        )
    else:  # openai
        model = st.selectbox(
            "Select Model",
            options=["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo"],
            index=0
        )
    
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.0,
        step=0.1,
        help="Higher values make output more random, lower values more deterministic"
    )
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown("This agent can help you with:")
    st.markdown("- Basic math operations (add, subtract, multiply, divide)")
    st.markdown("- Trigonometric functions (sine, cosine, tangent)")
    st.markdown("- General questions")
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything... (e.g., 'What is 25 + 37?')"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response with spinner
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Run the async agent_instance function
                response = asyncio.run(agent_instance(provider, model, prompt, temperature))
                st.markdown(response)
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                error_message = f"❌ Error: {str(e)}"
                st.error(error_message)
                st.session_state.messages.append({"role": "assistant", "content": error_message})

# Footer
st.markdown("---")
st.markdown(f"**Current Settings:** Provider: `{provider}` | Model: `{model}` | Temperature: `{temperature}`")
st.markdown("Built with Streamlit and LangChain MCP")


	

    