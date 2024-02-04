from django.shortcuts import render,redirect
from accounts.models import User,Shop 
from shopkeeper.models import Products

class AuthMiddleware2:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_id = request.session.get('user_id')
        if user_id is None and 'customers' in request.path:
            return render(request,'accessdenied.html')


        response = self.get_response(request)
        return response

