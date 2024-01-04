from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.vector_stores import ChromaVectorStore
from llama_index.storage.storage_context import StorageContext
from llama_index.embeddings import HuggingFaceEmbedding
from llama_index.llms import Ollama
import chromadb

# Load documents
documents = SimpleDirectoryReader("docs2").load_data()

llm = Ollama(model="deepseek-llm:7b-chat")

chroma_client = chromadb.EphemeralClient()
chroma_collection = chroma_client.create_collection("dbase")

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
service_context = ServiceContext.from_defaults(embed_model=embed_model, llm=llm)
index = VectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context,
    service_context=service_context,
)

query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
print(response)