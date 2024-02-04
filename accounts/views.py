from django.shortcuts import render,redirect
from accounts.models import Shop,User
from django.contrib.auth import logout as django_logout

# Create your views here.
def home(request):
     return render(request,'home.html')

def register_shop(request):
    if request.method == "POST" :
        name=request.POST['name']
        phone=request.POST['phone']
        password=request.POST['password']
        shop_name=request.POST['shop_name']
        shop_address=request.POST['shop_address']
        city=request.POST['city']
        color=request.POST['color']
        shop=Shop(owner=name,phone=phone,password=password,shop_name=shop_name,color=color,shop_address=shop_address,city=city)
        shop.save()
        return render(request,'shop_login_accounts.html')
    return render(request,'shop_register_accounts.html')

def login_shop(request):
    if request.method == "POST":
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = Shop.objects.filter(phone=phone, password=password).first()
        if user is not None:    
                request.session['user_id'] = user.id
                return redirect('/shopkeeper/shop/')
        else:
            return render(request, 'shop_login_accounts.html')
    return render(request,'shop_login_accounts.html')


def logout_shop(request):
    django_logout(request)
    request.session.flush()
    return render(request,'shop_login_accounts.html')


def register(request):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        password=request.POST['password']
        email=request.POST['email']
        address=request.POST['address']
        city=request.POST['city']
        user=User(name=name,phone=phone,password=password,email=email,address=address,city=city)
        user.save()
        return render(request,'login_accounts.html')
    return render(request,'register_accounts.html')

def login(request):
    if request.method == "POST":
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = User.objects.filter(phone=phone, password=password).first()
        if user is not None:    
                request.session['user_id'] = user.id
                return redirect('/customers/home/')
        else:
            return render(request, 'login_accounts.html')
    return render(request,'login_accounts.html')


def logout(request):
    django_logout(request)
    request.session.flush()
    return render(request,'login_accounts.html')



def register_deliveryman(request):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        password=request.POST['password']
        email=request.POST['email']
        address=request.POST['address']
        city=request.POST['city']
        user=User(name=name,phone=phone,password=password,email=email,address=address,city=city)
        user.save()
        return render(request,'deliveryman_login_accounts.html')
    return render(request,'deliveryman_register_accounts.html')

def login_deliveryman(request):
    if request.method == "POST":
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = User.objects.filter(phone=phone, password=password).first()
        if user is not None:    
                request.session['user_id'] = user.id
                return redirect('/deliveryman/home_deliveryman/')
        else:
            return render(request, 'deliveryman_login_accounts.html')
    return render(request,'deliveryman_login_accounts.html')


def logout_deliveryman(request):
    django_logout(request)
    request.session.flush()
    return render(request,'deliveryman_login_accounts.html')

