from django.db import models
from accounts.models import User,Shop
from shopkeeper.models import Products

# Create your models here.
class Orders(models.Model):
    userid=models.CharField(max_length=30)
    customername=models.CharField(max_length=30)
    address=models.CharField(max_length=300)
    name=models.CharField(max_length=30)
    price=models.CharField(max_length=30)
    brand=models.CharField(max_length=30)
    size=models.CharField(max_length=30)
    category=models.CharField(max_length=30)
    owner=models.CharField(max_length=30)
    shopaddress=models.CharField(max_length=300)
    shopname=models.CharField(max_length=30)    
    city=models.CharField(max_length=30)
    ownercontact=models.CharField(max_length=30)
    customercontact=models.CharField(max_length=30)

class Review(models.Model):
    user=models.ForeignKey('accounts.User',on_delete=models.CASCADE)
    product=models.ForeignKey('shopkeeper.Products',on_delete=models.CASCADE)
    review=models.CharField(max_length=300)
    rate=models.CharField(max_length=30)