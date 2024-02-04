from django.db import models

# Create your models here.

class Shop(models.Model):
    owner=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    shop_name=models.CharField(max_length=30)
    shop_address=models.CharField(max_length=250)
    city=models.CharField(max_length=30)
    color=models.CharField(max_length=30)
    
     
class User(models.Model):
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    address=models.CharField(max_length=250)
    city=models.CharField(max_length=30)    