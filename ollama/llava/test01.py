import ollama
res = ollama.chat(
    model="llava",
    messages=[{
            "role": "user", 
            'content': 'What are in the image?',
            'images':['bikini.jpg']
    }]
)

print(res['message']['content'])
