from django.shortcuts import render
from Fastshop.models import Orders
from accounts.models import User

# Create your views here.
def home_deliveryman(request):
    user_id=request.session.get('user_id')
    users=User.objects.get(id=user_id)
    city=users.city
    orders=Orders.objects.filter(city=city)
    return render(request,'home_deliveryman.html',{'orders':orders})