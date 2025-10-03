import requests

HOST = '127.0.0.1'
PORT = 8080

url = f"http://{HOST}:{PORT}"

response = requests.get(url)
print("GET response:", response.status_code)