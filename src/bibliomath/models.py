from pydoc import describe
from uuid import uuid4
from django.db import models
from django.urls import reverse
from djongo import models
from colorfield.fields import ColorField

# Create your models here.
class Resource(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    topic = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('resource-detail', kwargs={'pk': self.pk})

class Topic(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    color = ColorField(default='#FF0000')
    
    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('topic-detail', kwargs={'slug': self.title})

class Puzzle(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=50, unique=True)
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('puzzle-detail', kwargs={'slug': self.title})
