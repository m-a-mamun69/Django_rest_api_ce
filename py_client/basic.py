# Python API Client
import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoint, json={"title":"Hello World", "content":"This is Content"})    # HTTP Request

# print(get_response.text)  # print raw text response
# print(get_response.status_code)

print(get_response.json())
# print(get_response.json()['message'])
# print(get_response.status_code)