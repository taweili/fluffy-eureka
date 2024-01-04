from langchain.llms import Ollama 
from langchain.chat_models import ChatOllama

llm = Ollama(model="deepseek-llm:7b-chat")

response = llm.invoke("What's the capital of China?")
print(response)

chat_model = ChatOllama(model="deepseek-llm:7b-chat")

