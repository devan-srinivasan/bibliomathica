from distutils.command.upload import upload
from statistics import mode
from django.db import models
from djongo import models
from django.contrib.auth.models import User
from bibliomath.models import Resource
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile' 

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Collection(models.Model):
    _id = models.ObjectIdField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resources = models.ManyToManyField(Resource)

    def __str__(self):
        return f'{self.user.username} Collection' 