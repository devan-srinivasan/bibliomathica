from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.explore, name='explore'),
    path('puzzle/', TemplateView.as_view(template_name='puzzle.html'), name='puzzle'),
    path('explore/', views.explore, name='explore'),
    path('base/', TemplateView.as_view(template_name='base.html'), name='base'),    # to be deleted
]
