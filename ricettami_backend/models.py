from django.db import models
from django.urls import reverse

# Create your models here. 


class PersonalCard(models.Model):
   # Fields
    title = models.CharField(max_length=80) 
    description = models.CharField(max_length=150) 
    content = models.CharField(max_length=600)

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'content': self.content,
        }

class CommunityCard(models.Model):
   # Fields
    title = models.CharField(max_length=20) 
    description = models.CharField(max_length=150) 
    content = models.CharField(max_length=600)

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'content': self.content,
        }

class AICard(models.Model):
   # Fields
    title = models.CharField(max_length=20) 
    description = models.CharField(max_length=150) 
    content = models.CharField(max_length=600)

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'content': self.content,
        }