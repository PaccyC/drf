import requests


endpoint= "http://127.0.0.1:8000/api/products/6/update/"

data={
    "title":"Hello World Again",
    "content":"This is just greeting you all"
    
}
get_response=requests.put(endpoint,json=data)


print(get_response.status_code)
print(get_response.json())