from pydoc import describe
from django.db import models

# Create your models here.
class Resource(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    topic = models.CharField(max_length=50)

    def __str__(self):
        return self.title