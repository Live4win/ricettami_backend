from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.

@api_view(['GET', 'POST'])
def myapp(request):
    return Response({"someKey":"someValue"})

@api_view(['GET', 'POST'])
def login_user(request):
    username = "pincoPallino"# request.POST["username"]
    password = "sferaRotonda010" # request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({'loginResult': 'IS LOGGED IN PINCOPALLINO'})
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        return Response({'loginResult': 'false and failed'})

@api_view(['GET', 'POST'])
def logout_user(request):
    logout(request)
    return Response({"Result": "LOGOUT EXECUTED SUCCESSFULLY"})
    

@api_view(['GET', 'POST'])
def register_user(request):
    username = 'someNewUser' # request.data.get('username')
    password ='sferaRotonda01' # request.data.get('password')

    if not username or not password :
        return Response({'error': 'Please provide username, password, and email'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=400)

    user = User.objects.create(
        username=username,
        password=make_password(password),
        # email=emailsferaRotonda01sferaRotonda01sferaRotonda01sferaRotonda01sferaRotonda01sferaRotonda01sferaRotonda01sferaRotonda01sferaRotonda01sferaRotonda01sferaRotonda01sferaRotonda01sferaRotonda01sferaRotonda01sferaRotonda01sferaRotonda01sferaRotonda01sferaRotonda01
    )
    user.save()

    return Response({'success': 'User registered successfully'})