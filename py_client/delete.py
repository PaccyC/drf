import requests

product_id=input("What is the product id do you wanna use?\n")
try:
    product_id= int(product_id)
except:
    print(f'{product_id} is not valid')

if product_id:        

 endpoint= f"http://127.0.0.1:8000/api/products/{product_id}/delete/"

get_response=requests.delete(endpoint)


print(get_response.status_code)
print(get_response.status_code,get_response.status_code==204 )