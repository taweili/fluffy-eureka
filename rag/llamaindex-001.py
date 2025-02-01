from llama_index.llms.ollama import Ollama

llm = Ollama(model="mistral")
response = llm.complete("Why is sky blue?")
print(response)

