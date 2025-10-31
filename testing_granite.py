from langchain_ollama import ChatOllama

llm = ChatOllama(
    model='granite4:1b',
    temperature=0.1,
    num_ctx=2048,
)

def test_llm():
    response = llm.invoke(
        'Say hello and introduce yourself briefly.'
    )
    print(f"Most recent response: {response.content}")
    
test_llm()
