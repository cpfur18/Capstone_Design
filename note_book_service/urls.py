from django.contrib import admin
from django.urls import path, include
from note_book_service import views
import board.views
app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<prod_id>/', views.product, name='prod_info'),
    path('recommend/', views.cmd, name='recommend'),
    path('recommend/result/', views.recr, name='rec_result'),
    path('recommend/result/<prod_id>', views.product, name='rec_result_info'),
    path('community/', views.comm, name='community'),
    path('postinfo/', views.pstif, name='postinfo'),
    path('write/', views.wrt, name='write'),
    # path('expolre/<prod_id>/', views.expolre, name=''),
    path('getApi', views.getApi, name='getapi'),
    path('apiTest', views.apiTest, name='apiTest'),
    path('board/create', board.views.create),
    path('board/list', board.views.list),

    # path('coding/', views),
    # path('video_edit/', views),
    # path('office/', views),
    # path('select-tab/<str:tab-purpose>', views.index)
    #path('recommend/', include('sign.urls')),
    # path('search/', views.SearchFormView.as_view(), name='search'),
]
