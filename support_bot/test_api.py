import requests
import json

url = "http://127.0.0.1:8000/ask"
headers = {"Content-Type": "application/json"}
data = {"query": "Do I need planning permission?"}

response = requests.post(url, headers=headers, json=data)
print("Status Code:", response.status_code)
print("Response:", response.json()) 