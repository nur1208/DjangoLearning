from urllib import request
import requests

endpoint = "http://127.0.0.1:8000/v1/api"

response = requests.get(endpoint)

print(response.json())
print(response.status_code)


