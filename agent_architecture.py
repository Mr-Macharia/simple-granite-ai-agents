from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

SYSTEM_PROMPT = """You are a helpful AI assistant named Alex."""

class BasicAgent:
    def __init__(self):
        self.llm = ChatOllama(
            model="granite4:1b",
            temperature=0.1    
        )
        self.system_prompt = SystemMessage(
            content=SYSTEM_PROMPT
        )
    
    def chat(self, user_message):
        messages = [
            self.system_prompt,
            HumanMessage(content=user_message)
        ]
        response = self.llm.invoke(messages)
        return response.content

# Create and test your first agent
agent = BasicAgent()