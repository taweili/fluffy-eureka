package main

import (
	"context"
	"fmt"
	"log"

	"github.com/tmc/langchaingo/llms/ollama"
)

func main() {
	// Create a new instance of ollama with the model "mistral"
	llm, err := ollama.New(ollama.WithModel("mistral"))
	// If there is an error in creating the instance, log the error and stop the execution
	if err != nil {
		log.Fatal(err)
	}

	query := ""
	fmt.Println("Please enter your query: ")
	fmt.Scanln(&query)
	fmt.Println("Your query is: " + query)

	ctx := context.Background()
	completion, err := llm.Call(ctx, query)

	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Response:\n", completion)

}
