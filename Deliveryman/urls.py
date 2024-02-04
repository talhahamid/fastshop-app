from django.urls import path
from . import views

urlpatterns = [
    path('home_deliveryman/',views.home_deliveryman,name='home_deliveryman'),
]
