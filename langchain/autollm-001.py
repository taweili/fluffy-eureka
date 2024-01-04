from autollm import AutoQueryEngine, read_files_as_documents

documents = read_files_as_documents("./docs")

llm_model = "ollama/mistral"
llm_api_base = "http://localhost:11434"
query_engine = AutoQueryEngine.from_defaults(
    llm_model=llm_model,
    llm_api_base=llm_api_base,
    documents=documents,
    embed_model="local"
)

response =  query_engine.query(
    "在贵州有哪些项目？"
)

print("Response:" + response.response)
# print the detail of response 
print(response)
