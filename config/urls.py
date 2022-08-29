from django.contrib import admin
from django.urls import path, include
from note_book_service import views
import board.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('note_book_service.urls')),
    path('', include('sign.urls')),
    #path('abc/', board.views.abc),
    #path('getpost/write', board.views.getpostwrite),
    path('board/create', board.views.create),
    #path('board/list', board.views.list),
    #path('board/read/<int:bid>', board.views.read),
    #path('board/delete/<int:bid>', board.views.delete),
    #path('board/update/<int:bid>', board.views.update),
    path('', views.index, name='index'),
    
]
