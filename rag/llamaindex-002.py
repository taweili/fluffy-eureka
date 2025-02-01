from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

documents = SimpleDirectoryReader('paul').load_data()

Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")                                            

Settings.llm = Ollama(model="glm4", request_timeout=360)

index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()

response = query_engine.query("What is the main topic of this document?")                                   
print(response)
print("---")

response = query_engine.query("What did Paul do growing up?") 
print(response)
print("---")

response = query_engine.query("What languages have Paul used?")
print(response)
print("---")

response = query_engine.query("What is Paul's opinion on AI?")
print(response)
print("---")
