
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'sign'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='sign/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='sign/login.html'), name='logout'),
    path('register/', views.signup, name='register'),
]
