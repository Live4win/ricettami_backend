from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from . import models

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

@api_view(['GET', 'POST'])
def get_cards_personal(request):
    return Response({ 'isSuccess': True,'data': PersonalCard.objects})

@api_view(['GET', 'POST'])
def get_cards_community(request):
    return Response({ 'isSuccess': True,'data': CommunityCard.objects})

@api_view(['GET', 'POST'])
def get_cards_ai(request):
    return Response({ 'isSuccess': True,'data': AICard.objects})

@api_view(['GET', 'POST'])
def new_card_personal(request):
    title = 'title' # request.data.get('title')
    description ='descriptionPersonal' # request.data.get('description')
    content = 'some content' # 'request.data.get('content')'
    id = 0 # 'request.data.get('id')'

    if PersonalCard.objects.filter(id=id).exists():
        return Response({'isSuccess': False, 'data': 'This personal card already exists'}, status=400)

    personalCard = PersonalCard.objects.create(
        title = title,
        description = description,
        content = content,
        id = id
    )

    personalCard.save()

    return Response({ 'isSuccess': True,'data': personalCard})

@api_view(['GET', 'POST'])
def new_card_community(request):
    title = 'title' # request.data.get('title')
    description ='descriptionCommunity' # request.data.get('description')
    content = 'some content' # 'request.data.get('content')'
    id = 0 # 'request.data.get('id')'
    
    if CommunityCard.objects.filter(title=title).exists():
        return Response({'isSuccess': False, 'data': 'This community card already exists'}, status=400)

    communityCard = CommunityCard.objects.create(
        title = title,
        description = description,
        content = content,
        id = id
    )

    communityCard.save()

    return Response({ 'isSuccess': True,'data': communityCard})

@api_view(['GET', 'POST'])
def new_card_ai(request):
    title = 'title' # request.data.get('title')
    description ='descriptionAI' # request.data.get('description')
    content = 'some content' # 'request.data.get('content')'
    id = 0 # 'request.data.get('id')'

    if AICard.objects.filter(title=title).exists():
        return Response({'isSuccess': False, 'data': 'This ai card already exists'}, status=400)

    aiCard = AICard.objects.create(
        title = title,
        description = description,
        content = content,
        id = id
    )

    aiCard.save()

    return Response({ 'isSuccess': True,'data': aiCard})

@api_view(['GET', 'POST'])
def update_card_personal(request):
    id = 0 # request.data.get('id')
    personalCard = PersonalCard.objects.filter(id=id)

    if personalCard.exists():
        
        personalCard.title = 'someUpdate' # request.data.get('title')
        personalCard.description = 'someUpdate' # request.data.get('description')
        personalCard.content = 'someUpdate' # request.data.get('content')

        personalCard.save()

        return Response({'isSuccess': True, 'data': personalCard})
    
    else:
        return Response({'isSuccess': False, 'data': 'This personal card does not exist'})

@api_view(['GET', 'POST'])
def update_card_community(request):
    id = 0 # request.data.get('id')
    communityCard = CommunityCard.objects.filter(id=id)

    if communityCard.exists():
        communityCard.title = 'someUpdate' # request.data.get('title')
        communityCard.description = 'someUpdate' # request.data.get('description')
        communityCard.content = 'someUpdate' # request.data.get('content')

        communityCard.save()

        return Response({'isSuccess': True, 'data': communityCard})
    
    else:
        return Response({'isSuccess': False, 'data': 'This community card does not exist'})

@api_view(['GET', 'POST'])
def update_card_ai(request):
    id = 0 # request.data.get('id')
    aiCard = AICard.objects.filter(id=id)

    if aiCard.exists():
        aiCard.title = 'someUpdate' # request.data.get('title')
        aiCard.description = 'someUpdate' # request.data.get('description')
        aiCard.content = 'someUpdate' # request.data.get('content')

        aiCard.save()

        return Response({'isSuccess': True, 'data': aiCard})
    
    else:
        return Response({'isSuccess': False, 'data': 'This AI card does not exist'})

@api_view(['GET', 'POST'])
def delete_card_ai(request):
    id = 0 # request.data.get('id')
    aiCard = AICard.objects.filter(id=id)

    if aiCard.exists():
        aiCard.title = 'someUpdate' # request.data.get('title')
        aiCard.description = 'someUpdate' # request.data.get('description')
        aiCard.content = 'someUpdate' # request.data.get('content')

        Users.objects.

        aiCard.save()

        return Response({'isSuccess': True, 'data': aiCard})
    
    else:
        return Response({'isSuccess': False, 'data': 'This AI card does not exist'})

    