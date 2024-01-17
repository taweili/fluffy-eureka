# Write a program to post to a url
import json
import requests

url = "http://example.com/api"  # Replace this with your target API url
data = {
    "key1": "value1",
    "key2": "value2"  # Replace these with the keys and values you want to send
}

response = requests.post(url, json=json.dumps(data))
if response.status_code == 200:
    output = "Success:\nResponse:\n{}".format(json.dumps(response.json()))
else:
    output = "Error:{}\nResponse:{}\nData:{}".format(response.status_code, json.dumps(response.json()), json.dumps(data))

print(output)

