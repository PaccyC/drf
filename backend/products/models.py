from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

# User=settings.AUTH_USER_MODEL
class Products(models.Model):
    user=models.ForeignKey(User,default=1,on_delete=models.SET_NULL,null=True)
    title=models.CharField(max_length=120)
    content=models.TextField(blank=True,null=True)
    price= models.DecimalField(max_digits=15,decimal_places=2,default=99.99)
    
    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)