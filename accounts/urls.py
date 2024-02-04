from django.urls import path
from . import views

urlpatterns = [
    path('login_shop/',views.login_shop,name='login_shop'),
    path('register_shop/',views.register_shop,name='register_shop'),
    path('logout_shop/',views.logout_shop,name='logout_shop'),

    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),

    path('login_deliveryman/',views.login_deliveryman,name='login_deliveryman'),
    path('register_deliveryman/',views.register_deliveryman,name='register_deliveryman'),
    path('logout_deliveryman/',views.logout_deliveryman,name='logout_deliveryman'),

    path('',views.home,name='home'),

]
