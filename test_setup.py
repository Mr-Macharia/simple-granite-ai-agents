import ollama

# test ollama connection
response = ollama.generate(
    model= 'granite4:1b',
    prompt= 'Say hello and introduce yourself briefly.'
)

print(response['response'])