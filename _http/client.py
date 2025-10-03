import requests

url = "http://127.0.0.1:8080"

response = requests.get(url)
print("GET response:", response.status_code)