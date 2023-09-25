from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Products

def validate_title(value):
      qs=Products.objects.filter(title__iexact=value)
      if qs.exists():
        raise serializers.ValidationError(f"{value} is already a product name")
      return  value
  
def validate_title_no_hello(value):
    if "Hello" in value.lower():
        raise serializers.ValidationError(f"Hello is already a product name")
    return value

unique_product_title=UniqueValidator(queryset=Products.objects.all())
          
       