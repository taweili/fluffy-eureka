from langchain.document_loaders import TextLoader
from langchain.embeddings import OllamaEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.chroma import Chroma
import pprint

pp = pprint.PrettyPrinter(indent=4)

loader = TextLoader(r"C:\Users\david\Work\llm-query\docs2\winston.txt")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=10)
docs = text_splitter.split_documents(documents)

OLLAMA_MODEL="deepseek-llm:7b-chat"
embedding_function = OllamaEmbeddings(model=OLLAMA_MODEL)

db = Chroma.from_documents(docs, embedding_function)

query = "Where does Winston live"
docs = db.similarity_search_with_relevance_scores(query)

# iterate through docs and print each 
for doc, score in docs:
    print(f"----- {type(score)}: {score}")
    pp.pprint(doc)

