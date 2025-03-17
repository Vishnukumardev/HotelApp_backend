from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

from api.models import *

def home(request):
    return render(request, "home.html")  # Render the home page

@api_view(['GET'])
def hello(request):
    return Response({"message": "Hello, authenticated user!"})

##AUTHENTICATION ##
@api_view(['POST'])
def login(request):
    # Implement JWT login logic here
    return Response({"message": "Login logic goes here!"})

@api_view(['POST'])
def signup(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    if CustomUser.objects.filter(username=username).exists():
        return Response({"error": "Username already exists"}, status=400)

    hashed_password = make_password(password)  # Hash password before storing
    CustomUser = CustomUser.objects.create(username=username, password=hashed_password, email=email)
    user
    user.save()
    return Response({"message": "User created successfully!"})
##DASHBOARD##
##ROOMS##
##BOOKINGS##
##PAYMENTS##
##PROFILE##
##COMMUNICATION##
##ADMIN##
##REPORTS##
##SETTINGS##
##HELP##
##ERRORS##
##TEST##
##DEBUG##
##EXTERNAL##
##DEVELOPER##
##DEMO##
##OTHER##
##EXPERIMENTAL##
##CUSTOM##