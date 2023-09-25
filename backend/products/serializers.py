from rest_framework import serializers
from .models import Products
from .validators import validate_title_no_hello,unique_product_title

class ProductSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(write_only=True)
    
     # custom validation
    title=serializers.CharField(validators=[validate_title_no_hello,
                                            unique_product_title])

    class Meta:
        model = Products
        fields = [
            "pk",
            "user",
            "title",
            "content",
            "price",
            "sale_price"
        ]
   
        

        
   
   
   
#    Creating  create & update methods

    # def create(self, validated_data):
    #     # Extract the "email" field from validated_data
    #     email = validated_data.pop('email')

    #     # Create the Products object without the "email" field
    #     product = Products.objects.create(**validated_data)

    #     # Now, you can set the "email" field separately
    #     product.email = email

    #     # Save the object with the "email" field
        
    #     product.save()
    #     print(product,product.email)
       
    #     return product
    # def update(self, instance, validated_data):
    #    instance.title=validated_data.get("title")
    #    return instance
