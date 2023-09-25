from rest_framework import generics,mixins,permissions,authentication

from .models import Products
from .serializers import ProductSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from api.permissions import IsStaffEditorPermissions
from api.authentication import TokenAuthentication

from api.mixins import StaffEditorPermissionMixin

class ProductMixinView(generics.GenericAPIView,
                       mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin,
                       mixins.ListModelMixin):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    
    def get(self, request, *args, **kwargs):
        print({"args":args,"kwargs":kwargs})
        pk=kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
       
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        print(serializer)
        title= serializer.validated_data.get('title')
    
        content =serializer.validated_data.get('content') or None
        if content is None:
            content="This is the single view creating cool things"
            
        
        serializer.save(content=content)
    
    def update(self,request,*args,**kwargs):
        pk=kwargs.get("pk")
        if pk is not None:
            return self.update(request,*args,**kwargs)
       
    
    def destroy(self,request,*args,**kwargs):
        pk=kwargs.get("pk")
        if pk is not None:
             return self.destroy(request,*args,**kwargs)
            

class CreateProductListAPIView(generics.ListCreateAPIView,
                               StaffEditorPermissionMixin):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    permission_classes=[permissions.IsAdminUser,IsStaffEditorPermissions]
   
    def perform_create(self, serializer):
        print(serializer)
        title= serializer.validated_data.get('title')
    
        content =serializer.validated_data.get('content') or None
        if content is None:
            content=title
            
        
        serializer.save(user=self.request.user,content=content)
    def get_queryset(self):
        qs=super().get_queryset()  
        request=self.request
        user=request.user
        if not user.is_authenticated:
            return Products.objects.none()    
        return qs.filter(user=request.user)  

class ProductDetailAPIView(generics.RetrieveAPIView,
                           StaffEditorPermissionMixin):
    queryset= Products.objects.all()
    serializer_class=ProductSerializer
    
    

class ProductDetailListAPIView(generics.ListAPIView,
                               StaffEditorPermissionMixin):
    queryset= Products.objects.all()
    serializer_class=ProductSerializer    


@api_view(["GET","POST"])
def product_alt_view(request,pk=None,*args,**kwargs):
    method=request.method
    
    if method == "GET":
      if pk is not None:
        #detail view
    # if pk is not None:
    #    queryset=Products.objects.filter(pk=pk)
    #    if not queryset.exists():
    #        raise Http404()
        
        
        # Another way
  
       obj =get_object_or_404(Products,pk=pk)
       data=ProductSerializer(obj,many=False).data
       return Response(data)
    
    
        
        # list view
    if method == "GET":
        queryset=Products.objects.all()
        data=ProductSerializer(queryset,many=True).data
        return Response(data)
    
        
        
        
        # create view
    if method == "POST":
 
       serializer= ProductSerializer(data=request.data)
       if serializer.is_valid(raise_exception=True):
           print(serializer.data)
           title= serializer.validated_data.get('title')
    
           content =serializer.validated_data.get('content') or None
           if content is None:
            content=title
            
        
            serializer.save(content=content)

       return Response(serializer.data)
    return Response({"invalid data":"data is not good"},status=400)
            
         
         
class ProductUpdateAPIView(generics.UpdateAPIView,
                           StaffEditorPermissionMixin):
    queryset= Products.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'    
    
    def perform_update(self, serializer):
        instance=serializer.save()
        if not instance.content:
            instance.content=instance.title
   
            
class ProductDeleteAPIView(generics.DestroyAPIView,
                           StaffEditorPermissionMixin):
    queryset= Products.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'    
    
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
                     