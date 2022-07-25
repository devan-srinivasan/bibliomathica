from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import ResourceListView, ResourceDetailView, ResourceCreateView, ResourceUpdateView, ResourceDeleteView

urlpatterns = [
    path('', views.explore, name='explore'),
<<<<<<< HEAD
=======
    path('puzzle/', TemplateView.as_view(template_name='puzzle.html'), name='puzzle'),
    path('explore/', views.explore, name='explore'),
    #path('collection/', views.collection, name='collection'),
>>>>>>> e4a66e9e99f3c093d42a4b9b54c0c4fcbdb56c56
    path('sudo/', ResourceListView.as_view(), name='sudo'),
    path('sudo/<int:pk>', ResourceDetailView.as_view(), name='resource-detail'),
    path('sudo/new/', ResourceCreateView.as_view(), name='resource-create'),
    path('sudo/<int:pk>/update/', ResourceUpdateView.as_view(), name='resource-update'),
    path('sudo/<int:pk>/delete/', ResourceDeleteView.as_view(), name='resource-delete'),
    path('puzzle/', TemplateView.as_view(template_name='puzzle.html'), name='puzzle'),
    path('explore/', views.explore, name='explore'),
    path('collection/', views.collection, name='collection'),
    path('create_resource/', views.create_resource, name='create_resource'),
    path('create_topic/', views.create_topic, name='create_topic'),
    path('create_puzzle/', views.create_puzzle, name='create_puzzle'),
    path('get_all_puzzles/', views.get_all_puzzles, name='get_all_puzzles'),
    path('check_answer/', views.check_answer, name="check_answer")
]
