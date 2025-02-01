import requests
import os

# OpenAI API endpoint
OPENAI_URL = "http://127.0.0.1:11434/v1/chat/completions"

# Define the prompt
prompt = "why sky is blue"

# Create the request payload
payload = {
    "model": "text-davinci-003",
    "prompt": prompt,
    "max_tokens": 100,
    "temperature": 0.7
}

# Set up headers with API key
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer YOUR_API_KEY_HERE"  # User should replace with their key
}

try:
    # Send the request to OpenAI
    response = requests.post(OPENAI_URL, json=payload, headers=headers)
    response.raise_for_status()
    
    # Get and print the response
    result = response.json()
    print(result["choices"][0]["text"].strip())
    
except requests.exceptions.RequestException as e:
    print(f"Error connecting to OpenAI API: {e}")
