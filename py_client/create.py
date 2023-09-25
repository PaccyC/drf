import requests

headers= {'Authorization':'Bearer 25773e3df53e3eaa3b3f7e1fd928cd384778a166'}

endpoint= "http://127.0.0.1:8000/api/products/"

data={
    "title":"This is the title"
}
get_response=requests.post(endpoint,json=data,headers=headers)


print(get_response.status_code)
print(get_response.json())