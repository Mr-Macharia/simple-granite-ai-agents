from agent_architecture import BasicAgent

class SmartAgent(BasicAgent):
    def chat(self, user_message):
        
        if "calculate" in user_message.lower() or "math" in user_message.lower():
            return self.handle_math(user_message)
        elif "time" in user_message.lower() or "date" in user_message.lower():
            return self.handle_time(user_message)
        else:
            return super().chat(user_message)
        
        
    def handle_math(self, message):
        return "I can help with math calculations! Please provide the specific problem you'd like me to solve."
    
    def handle_time(self, message):
        import datetime
        now = datetime.datetime.now()
        return f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}"
    
Smart_agent = SmartAgent()
print(Smart_agent.chat("What is 5 + 7?"))
print(Smart_agent.chat("What is the current time?"))