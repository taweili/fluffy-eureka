from llama_index.llms import Ollama
from llama_index.embeddings import OllamaEmbedding
from llama_index import SimpleDirectoryReader, VectorStoreIndex, ServiceContext
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

OLLAMA_MODEL="deepseek-llm:7b-chat"
llm = Ollama(model=OLLAMA_MODEL)
embed_model = OllamaEmbedding(model_name=OLLAMA_MODEL)
service_context = ServiceContext.from_defaults(llm=llm, embed_model=embed_model)

documents = SimpleDirectoryReader("./docs").load_data()
index = VectorStoreIndex.from_documents(documents, service_context=service_context)
query_engine = index.as_query_engine()

resp = query_engine.query("list 10 things about Shanzhai")
print(resp)

resp = query_engine.query("Where is the term Shanzhai come from?")
print(resp)
