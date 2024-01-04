from langchain.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
model = ChatOllama(model="deepseek-llm:7b-chat")
output_parser = StrOutputParser()

chain = prompt | model | output_parser

res = chain.invoke({"topic": "ice cream"})

print(res)
