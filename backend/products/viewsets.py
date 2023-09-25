from rest_framework import viewsets,mixins
from .serializers import ProductSerializer
from .models import Products


class ProductViewSet(viewsets.ModelViewSet):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'
    
    

class ProductGenericViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'
    