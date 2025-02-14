from django.urls import path 
from . import views

urlpatterns = [
    path('api/', views.myapp),
    path('api/login/', views.login_user, name="login"),
    path('api/logout/', views.logout_user, name="logout"),
    path('api/register/', views.register_user, name= "register"),
]

