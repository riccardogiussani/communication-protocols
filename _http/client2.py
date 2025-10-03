import requests

HOST = '127.0.0.1'
PORT = 8080

url = f"http://{HOST}:{PORT}"

data = {"message": "Hello from Python HTTP client"}
response = requests.post(url+"/my_api_endpoint", data=data)
print("POST response:", response.text)
