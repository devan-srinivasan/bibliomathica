from django.contrib import admin
from .models import Collection, Profile
# Register your models here.

admin.site.register(Profile)
admin.site.register(Collection)