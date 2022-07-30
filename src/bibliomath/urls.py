from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import ResourceDetailView, ResourceCreateView, ResourceUpdateView, ResourceDeleteView
from .views import TopicDetailView, TopicCreateView, TopicUpdateView, TopicDeleteView
from .views import PuzzleDetailView, PuzzleCreateView, PuzzleUpdateView, PuzzleDeleteView

urlpatterns = [
    path('', views.explore, name='explore'),
    path('sudo/', views.sudo, name='sudo'),
    #sudo resources
    path('sudo/resource/<int:pk>', ResourceDetailView.as_view(), name='resource-detail'),
    path('sudo/new-resource/', ResourceCreateView.as_view(), name='resource-create'),
    path('sudo/resource/<int:pk>/update/', ResourceUpdateView.as_view(), name='resource-update'),
    path('sudo/resource/<int:pk>/delete/', ResourceDeleteView.as_view(), name='resource-delete'),
    #sudo topics
    path('sudo/topic/<slug:slug>', TopicDetailView.as_view(), name='topic-detail'),
    path('sudo/new-topic/', TopicCreateView.as_view(), name='topic-create'),
    path('sudo/topic/<slug:slug>/update/', TopicUpdateView.as_view(), name='topic-update'),
    path('sudo/topic/<slug:slug>/delete/', TopicDeleteView.as_view(), name='topic-delete'),
    #sudo puzzles
    path('sudo/puzzle/<slug:slug>', PuzzleDetailView.as_view(), name='puzzle-detail'),
    path('sudo/new-puzzle/', PuzzleCreateView.as_view(), name='puzzle-create'),
    path('sudo/puzzle/<slug:slug>/update/', PuzzleUpdateView.as_view(), name='puzzle-update'),
    path('sudo/puzzle/<slug:slug>/delete/', PuzzleDeleteView.as_view(), name='puzzle-delete'),

    path('puzzle/', TemplateView.as_view(template_name='puzzle.html'), name='puzzle'),
    path('explore/', views.explore, name='explore'),
    path('explore/<str:title>/', views.topic, name='topic'),
    path('create_resource/', views.create_resource, name='create_resource'),
    path('create_topic/', views.create_topic, name='create_topic'),
    path('create_puzzle/', views.create_puzzle, name='create_puzzle'),
    path('get_all_puzzles/', views.get_all_puzzles, name='get_all_puzzles'),
    path('check_answer/', views.check_answer, name="check_answer"),
    path('explore/<str:title>/add-resource/<int:id>/', views.addResource, name='addResource'),
]
