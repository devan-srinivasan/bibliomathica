from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.explore, name='explore'),
    path('hello-world/', TemplateView.as_view(template_name='hello_world.html'), name='hello-world'),
    path('explore/', views.explore, name='explore'),
]
