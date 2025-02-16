from django.urls import path 
from . import views

urlpatterns = [
    path('api', views.myapp),
    path('api/login', views.login_user, name="login"),
    path('api/logout', views.logout_user, name="logout"),
    path('api/register', views.register_user, name= "register"),

    path('api/cards/personal', views.get_cards_personal, name= "getPersonal"),
    path('api/cards/personal/new', views.new_card_personal, name= "newPersonal"),
    path('api/cards/personal/update', views.update_card_personal, name= "updatePersonal"),
    path('api/cards/personal/delete', views.delete_card_personal, name= "deletePersonal"),

    path('api/cards/community', views.get_cards_community, name= "getCommunity"),
    path('api/cards/community/new', views.new_card_community, name= "newCommunity"),
    path('api/cards/community/update', views.update_card_community, name= "updateCommunity"),
    path('api/cards/community/delete', views.delete_card_community, name= "deleteCommunity"),

    path('api/cards/ai', views.get_cards_ai, name= "getAI"),
    path('api/cards/ai/new', views.new_card_ai, name= "newAI"),
    path('api/cards/ai/update', views.update_card_ai, name= "updateAI"),
    path('api/cards/ai/delete', views.delete_card_ai, name= "deleteAI"),
]

