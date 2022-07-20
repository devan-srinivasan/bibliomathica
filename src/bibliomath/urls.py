from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import ResourceListView, ResourceDetailView, ResourceCreateView, ResourceUpdateView, ResourceDeleteView

urlpatterns = [
    path('', views.explore, name='explore'),
    path('puzzle/', TemplateView.as_view(template_name='puzzle.html'), name='puzzle'),
    path('explore/', views.explore, name='explore'),
    path('collection/', ResourceListView.as_view(), name='collection'),
    path('collection/<int:pk>', ResourceDetailView.as_view(), name='resource-detail'),
    path('collection/new/', ResourceCreateView.as_view(), name='resource-create'),
    path('collection/<int:pk>/update/', ResourceUpdateView.as_view(), name='resource-update'),
    path('collection/<int:pk>/delete/', ResourceDeleteView.as_view(), name='resource-delete'),
    path('create_resource/', views.create_resource, name='create_resource'),
    path('create_topic/', views.create_topic, name='create_topic'),
]
