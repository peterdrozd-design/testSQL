import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "tinyllama", "prompt": "What is the capital of France?", "Stream": False}
)

# for line in response.iter_lines():
#     if line:
#         print(line.decode("utf-8"))

data = response.json()
print(data["response"])