from langgraph.prebuilt import create_react_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from tools import calculator, get_current_time

# Initialize LLM
llm = ChatOllama(
    model='granite4:1b',
    temperature=0.1,
    num_ctx=2048,
)

# Define tools
tools = [calculator, get_current_time]

try:
    # Create a ReAct agent
    agent = create_react_agent(llm, tools)

    # Send a message
    response = agent.invoke(
        {"messages": 
            [HumanMessage(content="What is the current time and what is 15 multiplied by 7?")]
        }
    )

    # Print the AI's response
    print(response["messages"][-1].content)

except Exception as e:
    print(f"An error occurred: {e}")
