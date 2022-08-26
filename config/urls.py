from django.contrib import admin
from django.urls import path, include
from note_book_service import views
import board.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('note_book_service.urls')),
    path('', include('sign.urls')),
    #path('abc/', board.views.abc),
    path('getpost/write', board.views.getpostwrite),
    path('', views.index, name='index'),
]
