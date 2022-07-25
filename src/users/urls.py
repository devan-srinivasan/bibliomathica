from django.urls import path, re_path, include
from django.views.generic import TemplateView
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', user_views.register, name="register"),
    path('profile/', user_views.profile, name="profile"),
    path('collection/', user_views.collection, name='collection'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
]
