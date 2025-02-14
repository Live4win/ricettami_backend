from django.db import models
from django.urls import reverse

# Create your models here. 


class PersonalCard(models.Model):
   # Fields
    title = models.CharField(max_length=20) 
    description = models.CharField(max_length=20) 
    content = models.CharField(max_length=20) 

class CommunityCard(models.Model):
   # Fields
    title = models.CharField(max_length=20) 
    description = models.CharField(max_length=20) 
    content = models.CharField(max_length=20) 

class CommunityCard(sto aco):
   # Fields
    title = models.CharField(max_length=20) 
    description = models.CharField(max_length=20) 
    content = models.CharField(max_length=20) 