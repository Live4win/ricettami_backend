from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import PersonalCard, CommunityCard, AICard
from django.core import serializers

# Create your views here.

@api_view(['GET', 'POST'])
def myapp(request):
    return Response({"someKey":"someValue"})

@api_view(['GET', 'POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({'loginResult': True, 'user': {'username': user.username, 'email': user.email}})
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        return Response({'loginResult': False})

@api_view(['GET', 'POST'])
def logout_user(request):
    logout(request)
    return Response({"Result": "LOGOUT EXECUTED SUCCESSFULLY"})
    

@api_view(['GET', 'POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password :
        return Response({'error': 'Please provide username and password'}, status=400)

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
    data = [card.to_json() for card in PersonalCard.objects.all()]
    return Response({'isSuccess': True, 'data': data})

@api_view(['GET', 'POST'])
def get_cards_community(request):
    data = [card.to_json() for card in CommunityCard.objects.all()]
    return Response({ 'isSuccess': True,'data': data})

@api_view(['GET', 'POST'])
def get_cards_ai(request):
    data = [card.to_json() for card in AICard.objects.all()]
    return Response({ 'isSuccess': True,'data': data})

@api_view(['GET', 'POST'])
def new_card_personal(request):
    title = 'title' # request.data.get('title')
    description ='descriptionPersonal' # request.data.get('description')
    content = 'some content' # 'request.data.get('content')'

    if PersonalCard.objects.filter(title=title).exists():
        return Response({'isSuccess': False, 'data': 'This personal card already exists'}, status=400)

    personalCard = PersonalCard.objects.create(
        title = title,
        description = description,
        content = content,
    )

    personalCard.save()

    return Response({ 'isSuccess': True, 'data': personalCard.to_json()})

@api_view(['GET', 'POST'])
def new_card_community(request):
    title = 'title' # request.data.get('title')
    description ='descriptionCommunity' # request.data.get('description')
    content = 'some content' # 'request.data.get('content')'
    
    if CommunityCard.objects.filter(title=title).exists():
        return Response({'isSuccess': False, 'data': 'This community card already exists'}, status=400)

    communityCard = CommunityCard.objects.create(
        title = title,
        description = description,
        content = content,
    )

    communityCard.save()

    return Response({ 'isSuccess': True,'data': communityCard.to_json()})

@api_view(['GET', 'POST'])
def new_card_ai(request):
    title = 'title' # request.data.get('title')
    description ='descriptionAI' # request.data.get('description')
    content = 'some content' # 'request.data.get('content')'

    if AICard.objects.filter(title=title).exists():
        return Response({'isSuccess': False, 'data': 'This ai card already exists'}, status=400)

    aiCard = AICard.objects.create(
        title = title,
        description = description,
        content = content,
    )

    aiCard.save()

    return Response({ 'isSuccess': True,'data': aiCard.to_json()})

@api_view(['GET', 'POST'])
def update_card_personal(request):
    id = 3 # request.data.get('id')
    personalCard = PersonalCard.objects.filter(id=id)

    if personalCard.exists():
        
        personalCard.update(
            title = 'someUpdate', # request.data.get('title')
            description = 'someUpdate', # request.data.get('description')
            content = 'someUpdate', # request.data.get('content')
        )

        # personalCard.save()

        return Response({'isSuccess': True, 'data': personalCard.values()}) # FIXED: converted to JSON
    
    else:
        return Response({'isSuccess': False, 'data': 'This personal card does not exist'})

@api_view(['GET', 'POST'])
def update_card_community(request):
    id = 3 # request.data.get('id')
    communityCard = CommunityCard.objects.filter(id=id)

    if communityCard.exists():

        communityCard.update(
            title = 'someUpdate', # request.data.get('title')
            description = 'someUpdate', # request.data.get('description')
            content = 'someUpdate', # request.data.get('content')
        )
        return Response({'isSuccess': True, 'data': communityCard.values()})
    
    else:
        return Response({'isSuccess': False, 'data': 'This community card does not exist'})

@api_view(['GET', 'POST'])
def update_card_ai(request):
    id = 1 # request.data.get('id')
    aiCard = AICard.objects.filter(id=id)

    if aiCard.exists():
        
        aiCard.update(
            title = 'someUpdate', # request.data.get('title')
            description = 'someUpdate', # request.data.get('description')
            content = 'someUpdate', # request.data.get('content')
        )

        return Response({'isSuccess': True, 'data': aiCard.values()})
    
    else:
        return Response({'isSuccess': False, 'data': 'This AI card does not exist'})
    

@api_view(['GET', 'POST'])
def delete_card_personal(request):
    id = 1 # request.data.get('id')
    personalCard = PersonalCard.objects.filter(id=id)

    if personalCard.exists():
        personalCard.delete()

        return Response({'isSuccess': True, 'data': None})
    
    else:
        return Response({'isSuccess': False, 'data': 'This personal card does not exist'})
    
@api_view(['GET', 'POST'])
def delete_card_community(request):
    id = 2 # request.data.get('id')
    communityCard = CommunityCard.objects.filter(id=id)

    if communityCard.exists():
        communityCard.delete()

        return Response({'isSuccess': True, 'data': None})
    
    else:
        return Response({'isSuccess': False, 'data': 'This community card does not exist'})

@api_view(['GET', 'POST'])
def delete_card_ai(request):
    id = 1 # request.data.get('id')
    aiCard = AICard.objects.filter(id=id)

    if aiCard.exists():
        aiCard.delete()

        return Response({'isSuccess': True, 'data': None})
    
    else:
        return Response({'isSuccess': False, 'data': 'This AI card does not exist'})
    


    