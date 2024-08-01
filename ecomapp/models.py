from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    user_type=models.CharField(default=1,max_length=10)
    

class category(models.Model):
    category=models.CharField(max_length=20,null=True)
    
class product(models.Model):
    category1=models.ForeignKey(category,on_delete=models.CASCADE,null=True)
    pname=models.CharField(max_length=25,null=True)
    desc=models.CharField(max_length=255,null=True)
    price=models.IntegerField(null=True)
    pimage=models.ImageField(upload_to="image/",null=True)
    
class usermember(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    dob=models.DateField(null=True)
    number=models.CharField(max_length=255,null=True)
    city=models.CharField(max_length=25,null=True)
    
class cart(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    prod=models.ForeignKey(product,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField(default=1)
    
    def total_price(self):
        return self.quantity*self.prod.price
    
