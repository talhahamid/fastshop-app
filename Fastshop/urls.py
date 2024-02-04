from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('categories/',views.categories,name='categories'),
    path('products/<int:id>/',views.products,name='products'),
    path('productdetails/<int:id>/',views.productsdetails,name='productsdetails'),
    path('bargain/<int:id>/<int:bargainrange>/<int:price>/',views.bargain,name='bargain'),
    path('buy/<int:id>/',views.buy,name='buy'),
    path('orders/',views.orders,name='orders'),
    path('cancelorder/<int:id>/',views.cancelorder,name='cancelorder'),
    path('deletereviews/<int:review_id>/<int:product_id>/',views.deletereviews,name='deletereviews'),


    path('',views.index,name='learning'),
]
