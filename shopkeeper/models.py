from django.db import models
# Create your models here.

class Products(models.Model):
    shop=models.ForeignKey('accounts.Shop',on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    image1=models.ImageField()
    image2=models.ImageField()
    image3=models.ImageField()
    image4=models.ImageField()
    brand=models.CharField(max_length=30)    
    price=models.CharField(max_length=30)
    quantity=models.CharField(max_length=30)
    category=models.CharField(max_length=30)
    size=models.CharField(max_length=30,default='null')
    forwhom=models.CharField(max_length=30,default='null')
    manufacture=models.DateField()
    bargainrange=models.CharField(max_length=30)
    description=models.CharField(max_length=1000)