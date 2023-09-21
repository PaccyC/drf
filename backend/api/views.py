
from django.forms.models import model_to_dict
from django.shortcuts import render
from products.serializers import ProductSerializer
from products.models import Products
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["POST"])
def api_home(request):
   instance={}
   
#    instance=Products.objects.all().order_by("?").first()
#    if instance:
  
#     #    data= model_to_dict(model_data,fields=["id","title","content","price","sale_price"])
     
#         data=ProductSerializer(instance).data
   serializer= ProductSerializer(data=request.data)
   if serializer.is_valid(raise_exception=True):
     instance=serializer.save()
     print(instance)
     return Response(serializer.data)
   return Response({"invalid data":"data is not good"},status=400)