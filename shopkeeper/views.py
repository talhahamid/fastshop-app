from django.shortcuts import render
from shopkeeper.models import Products
from accounts.models import Shop
# Create your views here.

def addproducts(request):
    if request.method=="POST":
        name=request.POST['name']
        image1=request.FILES['image1']
        image2=request.FILES['image2']
        image3=request.FILES['image3']
        image4=request.FILES['image4']
        brand=request.POST['brand']
        price=request.POST['price']
        quantity=request.POST['quantity']
        description=request.POST['description']
        owner=request.session.get('user_id')
        category=request.POST['category']
        size=request.POST['size']
        forwhom=request.POST['forwhom']
        bargainrange=request.POST['bargainrange']
        manufacture=request.POST['manufacturer']
        owner_id=request.session.get('shop_id')
        owner=Shop.objects.get(id=owner_id)
        product=Products(shop=owner,name=name,image1=image1,image2=image2,image3=image3,image4=image4,brand=brand,price=price,quantity=quantity,description=description,category=category,size=size,forwhom=forwhom,bargainrange=bargainrange,manufacture=manufacture)
        product.save()
        return render(request,'addproducts_shopkeeper.html')
    return render(request,'addproducts_shopkeeper.html')

def shop(request):
    owner=request.session.get('shop_id')
    products=Products.objects.filter(shop=owner)
    return render(request,'shop_shopkeeper.html',{'products':products})

def profile(request):
    user=request.session.get('shop_id')
    users=Shop.objects.filter(id=user)
    return render(request,'profile_shopkeeper.html',{'users':users})

def deleteproduct(request,id):
    product=Products.objects.get(id=id)
    product.delete()
    owner=request.session.get('shop_id')
    products=Products.objects.filter(shop=owner)
    return render(request,'shop_shopkeeper.html',{'products':products})