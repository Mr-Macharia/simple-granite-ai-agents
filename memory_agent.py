# memory_agent.py
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.sqlite import SqliteSaver
from tools import calculator as simple_calculator, get_current_time



# Setup: LLM, Tools, and SQLite Memory

tools = [simple_calculator, get_current_time]

llm = ChatOllama(
    model="granite4:1b",
    temperature=0.1,
    num_ctx=2048,
)

# Helper to safely extract the assistant message

def get_last_message(response):
    """
    Works for both LangGraph dict and LangChain object responses.
    """
    if isinstance(response, dict) and "messages" in response:
        messages = response["messages"]
    elif hasattr(response, "messages"):
        messages = response.messages
    else:
        return str(response)

    for msg in reversed(messages):
        # msg is a BaseMessage; extract .content if present
        content = getattr(msg, "content", None)
        if content:
            return content
    return "(no content found)"



# Run memory demo 
def run_memory_demo():
    # Context manager for SqliteSaver
    with SqliteSaver.from_conn_string(":memory:") as memory_store:
        # Create agent with SQLite checkpoint
        agent = create_agent(llm, tools, checkpointer=memory_store)

        config = {"configurable": {"thread_id": "user_123"}}

        print("=== Conversation 1 ===")
        resp1 = agent.invoke({"messages": [HumanMessage(content="My favorite color is 10 - 5.")]}, config=config)
        print("AI:", get_last_message(resp1))

        print("\n=== Conversation 2 ===")
        resp2 = agent.invoke({"messages": [HumanMessage(content="Calculate 12 * 7 using your calculator tool.")]}, config=config)
        print("AI:", get_last_message(resp2))

        print("\n=== Conversation 3 ===")
        resp3 = agent.invoke({"messages": [HumanMessage(content="What is the time now?")]}, config=config)
        print("AI:", get_last_message(resp3))

        print("\n=== Conversation 4 ===")
        resp4 = agent.invoke({"messages": [HumanMessage(content="What is my favorite color?")]}, config=config)
        print("AI:", get_last_message(resp4))


if __name__ == "__main__":
    run_memory_demo()
