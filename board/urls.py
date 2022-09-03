from django.urls import path, include
from . import views

app_name = 'board'

urlpatterns = [
    path('community/', views.comm, name='community'),
    path('postinfo/', views.pstif, name='postinfo'),
    path('write/', views.wrt, name='write'),
    path('board/create', views.create),
    path('board/list', views.list),
]
