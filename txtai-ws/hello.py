from txtai import Embeddings, LLM

def main():
    # Initialize txtai with Mistral model
    llm = LLM("ollama/mistral")
    
    # Ask the question
    response = llm("Why is the sky blue?")
    
    # Print the response
    print(response)

if __name__ == "__main__":
    main()
