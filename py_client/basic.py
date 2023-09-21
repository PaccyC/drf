import  requests

endpoint= "http://127.0.0.1:8000/api/"

get_response=requests.post(endpoint,params={"abc":"123"},json={"title":None,"content":"Hello world"})

print(get_response.text)
print(get_response.status_code)
print(get_response.json())