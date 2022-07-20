from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.explore, name='explore'),
    path('puzzle/', TemplateView.as_view(template_name='puzzle.html'), name='puzzle'),
    path('explore/', views.explore, name='explore'),
    path('collection/', views.collection, name='collection'),
    path('create_resource/', views.create_resource, name='create_resource'),
    path('create_topic/', views.create_topic, name='create_topic'),
]
