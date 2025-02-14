from django.db import models
from django.urls import reverse

# Create your models here. 


class PersonalCard(models.Model):
   # Fields
    title = models.CharField(max_length=80) 
    description = models.CharField(max_length=150) 
    content = models.CharField(max_length=600) 
    id = models.IntegerField(unique=True)

class CommunityCard(models.Model):
   # Fields
    title = models.CharField(max_length=20) 
    description = models.CharField(max_length=150) 
    content = models.CharField(max_length=600)
    id = models.IntegerField(unique=True)

class AICard(models.Model):
   # Fields
    title = models.CharField(max_length=20) 
    description = models.CharField(max_length=150) 
    content = models.CharField(max_length=600)
    id = models.IntegerField(unique=True)