from urllib import request
import requests

endpoint = "http://127.0.0.1:8000"

response = requests.get(endpoint)

print(response.status_code)


