import requests

url = "http://127.0.0.1:8080"

data = {"message": "Hello from Python HTTP client"}
response = requests.post(url+"/my_api_endpoint", data=data)
print("POST response:", response.text)
