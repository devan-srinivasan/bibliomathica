from django.contrib import admin
from .models import Puzzle, Resource, Topic

admin.site.register(Resource)
admin.site.register(Topic)
admin.site.register(Puzzle)
# Register your models here.
