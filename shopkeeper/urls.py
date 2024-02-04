from django.urls import path
from . import views

urlpatterns = [
    path('addproducts/',views.addproducts,name='addproducts'),
    path('shop/',views.shop,name='shop'),
    path('profile/',views.profile,name='profile'),
    path('deleteproduct/<int:id>/',views.deleteproduct,name='deleteproduct'),
]
