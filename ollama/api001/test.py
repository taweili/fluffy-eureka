import ollama 
response = ollama.chat(model="llama3", messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Why is the sky blue?"}
])
print(response['message']['content'])