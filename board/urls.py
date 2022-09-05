from django.urls import path, include
from . import views

app_name = 'board'

urlpatterns = [
    path('community/', views.comm, name='community'),
    path('postinfo/', views.pstif, name='postinfo'),
    path('write/', views.wrt, name='write'),
    path('board/create', views.create, name='create'),
    path('board/list', views.list),
    path('board/read/<int:bid>', views.read, name='read'),
    path('board/update/<int:bid>', views.update, name='update'),
    path('board/delete/<int:bid>', views.delete, name='delete'),
]
