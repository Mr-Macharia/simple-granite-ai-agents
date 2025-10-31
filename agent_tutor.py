from agent_architecture import BasicAgent
from langchain_core.messages import SystemMessage


class AITutor(BasicAgent):
   def __init__(self):
      super().__init__()
      self.knowledge_base = {
           "machine learning": "A method of data analysis that automates analytical model building.",
            "neural network": "Computing systems inspired by biological neural networks.",
            "deep learning": "A subset of machine learning that uses neural networks with many layers.", 
            "llm": "Large Language Model - AI trained on vast amounts of text data."
      }
      
      self.system_prompt = SystemMessage(
          content="You are an AI tutor specialized in Machine Learning from the knowledgebase provided. "
                   "otherwise provide general explanations. Be educational and clear."
      )
      
   def chat(self, user_message):
       
       for topic, definition in self.knowledge_base.items():
            if topic.lower() in user_message.lower():
                return f"{topic.title()}: {definition}"
            return super().chat(user_message)

    
tutor = AITutor()   
# print(tutor.chat("Can you explain machine learning?"))
# print(tutor.chat("What is a neural network?"))
print(tutor.chat("Tell me about deep learning."))
# print(tutor.chat("What is an llm?"))
# print(tutor.chat("How does photosynthesis work?"))
