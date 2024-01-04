import requests
import json

url = 'http://localhost:8000/chat/completions'
data = {
    'model': 'gpt-3.5',
    'messages': [
        {
            'role': 'user',
            'content': "write a python hello world program"
        }
    ]
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.text)