from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from accounts.models import Shop
from accounts.models import User
from Fastshop.models import Orders,Review
from shopkeeper.models import Products
from django.http import HttpResponse
from django.db.models import F, Value, CharField
# Create your views here.

def home(request):
    user=request.session.get('user_id')
    users=User.objects.get(id=user)
    city=users.city
    shops=Shop.objects.filter(city=city)
    return render(request,'home_customer.html',{'shops':shops})


def profile(request):
    user=request.session.get('user_id')
    user=User.objects.get(id=user)
    return render(request,'profile_customer.html',{'user':user})


def categories(request):
    if request.method == "GET":
        category = request.GET.get('category', '')
        size = request.GET.get('size', '')
        brand = request.GET.get('brand', '')
        price = request.GET.get('price', '')

        # Filtering based on provided parameters
        products = Products.objects.filter(
            category__icontains=category,
            size__icontains=size,
            brand__icontains=brand,
            price__icontains=price
        )
        return render(request, 'categories_customer.html', {'products': products})
    return render(request, 'categories_customer.html')

def products(request,id):
    products=Products.objects.filter(shop_id=id)
    return render(request,'products_customer.html',{'products':products})


def productsdetails(request, id):
    product = get_object_or_404(Products, id=id)
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id) if user_id else None
    if request.method == "POST":
        existing_review = Review.objects.filter(user=user, product=product).first()
        print(existing_review)
        if existing_review:
            message=("You has already submitted a review for this product.")
            reviews = Review.objects.filter(product=product)
            total_rating = 0
            for review in reviews:
                total_rating += int(review.rate)

            average_rating = total_rating / len(reviews) if len(reviews) > 0 else 0
            ratings=review.rate
            ratings=int(ratings)
            return render(request, 'productdetails_customer.html', {'product': product, 'reviews': reviews,'message':message,'average_rating':average_rating,'ratings':ratings})
        else:
            review_text = request.POST['review']
            rating = request.POST['rating']
            print(request.POST['rating'])
            message=""
            new_review = Review(user=user, product=product, rate=rating, review=review_text)
            new_review.save()
            reviews = Review.objects.filter(product=product)
            total_rating = 0
            for review in reviews:
                total_rating += int(review.rate)

            average_rating = total_rating / len(reviews) if len(reviews) > 0 else 0
            ratings=review.rate
            ratings=int(ratings)
            return render(request, 'productdetails_customer.html', {'product': product, 'reviews': reviews,'average_rating':average_rating,'ratings':ratings})
    reviews = Review.objects.filter(product=product)
    message=""
    total_rating = 0
    for review in reviews:
        total_rating += int(review.rate)

    average_rating = total_rating / len(reviews) if len(reviews) > 0 else 0
    ratings=review.rate
    ratings=int(ratings)
    return render(request, 'productdetails_customer.html', {'product': product, 'reviews': reviews,'message':message,'average_rating':average_rating,'ratings':ratings})



def deletereviews(request,review_id,product_id):
    reviews = Review.objects.filter(id=review_id)
    reviews.delete()
    return redirect(f'/customers/productdetails/{product_id}/')


def bargain(request,bargainrange,price,id):
    if request.method=="POST":
        bargain=request.POST['bargain']
        bargain=int(bargain)
        if price-bargainrange<=bargain:
            products=Products.objects.get(id=id)
            return render(request,'pay_customer.html',{'products':products})             
        else:
            if bargainrange==0:
                message="You cant burgain on this product"  
                return render(request,'bargain_customer.html',{'price':price,'bargainrange':bargainrange,'message':message}) 
            else: 
                message="Not possible! Please, bargain with better amount."
                return render(request,'bargain_customer.html',{'price':price,'bargainrange':bargainrange,'message':message})
    return render(request,'bargain_customer.html',{'id':id,'price':price,'bargainrange':bargainrange})

def buy(request,id):
    if request.method=="POST":
        address=request.POST['address']
        products=Products.objects.get(id=id)
        name=products.name
        price=products.price
        owner=products.shop.owner
        shopname=products.shop.shop_name
        shopaddress=products.shop.shop_address       
        category=products.category
        brand=products.brand
        size=products.size
        user_id=request.session.get('user_id')
        users=User.objects.get(id=user_id)    
        customername=users.name
        city=users.city
        ownercontact=products.shop.phone
        customercontact=users.phone
        orders=Orders(userid=user_id,customername=customername,customercontact=customercontact,ownercontact=ownercontact,city=city,address=address,shopaddress=shopaddress,shopname=shopname,name=name,price=price,owner=owner,category=category,brand=brand,size=size)
        orders.save()
        return redirect('/customers/orders/')

def orders(request):
    user_id=request.session.get('user_id')
    orders=Orders.objects.filter(userid=user_id)
    print(orders)
    return render(request,'buy_customer.html',{'orders':orders})

def cancelorder(request,id):
    order=Orders.objects.get(id=id)
    order.delete()
    user_id=request.session.get('user_id')
    orders=Orders.objects.filter(id=user_id)
    return render(request,'buy_customer.html',{'orders':orders})



def index(request):
    if request.method=="POST":
        rating=request.POST['rating']
        print(rating)
        user_id = request.session.get('user_id')
        user = User.objects.get(id=user_id) 
        product = Products.objects.get(id=3)

        new_review = Review(user=user, product=product, rate=rating)
        new_review.save()

        return render(request, 'demo.html')

    return render(request, 'demo.html')