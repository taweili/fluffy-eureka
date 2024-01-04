import os 
from haystack import Document
from haystack.document_stores import InMemoryDocumentStore
from haystack.pipeline_utils import build_rag_pipeline
from haystack.components.generators import GPTGenerator

gg = GPTGenerator(  api_base_url="http://localhost:8000/v1",
                    model_name="mistral",
                    api_key="xxx")

document_store = InMemoryDocumentStore()

documents = [
    Document(content="My name is Jane and I live in Paris"),
    Document(content="My name is Mark and I live in London"),
    Document(content="My name is Bill and I live in Berlin")    
]
document_store.write_documents(documents)

rag_pipeline = build_rag_pipeline()