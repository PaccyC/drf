import requests


endpoint= "http://127.0.0.1:8000/api/products/6"

get_response=requests.get(endpoint,params={"abc":"123"},json={"title":"HELLO","content":"Hello world"})


print(get_response.status_code)
print(get_response.json())