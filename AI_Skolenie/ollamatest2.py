import requests
import json

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"}
]

response = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "tinyllama",
        "messages": messages,
        "stream": False
    }
)

data = response.json()
print(data["message"]["content"])