# Python API Client
import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, json={"query":"Hello World"})    # HTTP Request

print(get_response.text)  # print raw text response

print(get_response.json())
print(get_response.status_code)