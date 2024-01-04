from django.urls import path, re_path
from django.views.generic import TemplateView
from . import views
from .views import ResourceDetailView, ResourceCreateView, ResourceUpdateView, ResourceDeleteView
from .views import TopicDetailView, TopicCreateView, TopicUpdateView, TopicDeleteView
from .views import PuzzleDetailView, PuzzleCreateView, PuzzleUpdateView, PuzzleDeleteView

REGEX_PATTERN = "(?P<slug>[\w\ \'\?]+)"
urlpatterns = [
    path('', views.explore, name='explore'),
    path('sudo/', views.sudo, name='sudo'),
    #sudo resources
    path('sudo/resource/<int:pk>/', ResourceDetailView.as_view(), name='resource-detail'),
    path('sudo/new-resource/', ResourceCreateView.as_view(), name='resource-create'),
    path('sudo/resource/<int:pk>/update/', ResourceUpdateView.as_view(), name='resource-update'),
    path('sudo/resource/<int:pk>/delete/', ResourceDeleteView.as_view(), name='resource-delete'),
    #sudo topics
    re_path(f'sudo/topic/{REGEX_PATTERN}/', TopicDetailView.as_view(), name='topic-detail'),
    path('sudo/new-topic/', TopicCreateView.as_view(), name='topic-create'),
    re_path(f'sudo/update-topic/{REGEX_PATTERN}/', TopicUpdateView.as_view(), name='topic-update'),
    re_path(f'sudo/delete-topic/{REGEX_PATTERN}/', TopicDeleteView.as_view(), name='topic-delete'),
    #sudo puzzles
    # re_path(f'sudo/puzzle/{REGEX_PATTERN}/', PuzzleDetailView.as_view(), name='puzzle-detail'),
    # path('sudo/new-puzzle/', PuzzleCreateView.as_view(), name='puzzle-create'),
    # re_path(f'sudo/update-puzzle/{REGEX_PATTERN}/', PuzzleUpdateView.as_view(), name='puzzle-update'),
    # re_path(f'sudo/delete-puzzle/{REGEX_PATTERN}/', PuzzleDeleteView.as_view(), name='puzzle-delete'),

    # path('puzzle/', views.puzzle, name='puzzle'),
    path('explore/', views.explore, name='explore'),
    path('explore/<str:title>/', views.topic, name='topic'),
    path('get_all_puzzles/', views.get_all_puzzles, name='get_all_puzzles'),
    path('check_answer/', views.check_answer, name="check_answer"),
    path('explore/<str:title>/add-resource/<int:id>/', views.addResource, name='addResource'),
]
