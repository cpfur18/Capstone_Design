from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('note_book_service/recommend.html/', views.cmd, name='recommend'),
    path('note_book_service/community.html/', views.comm, name='community'),
    path('expolre/<prod_id>/', views.expolre, name='prod_info'),
    # path('coding/', views),
    # path('video_edit/', views),
    # path('office/', views),
    # path('select-tab/<str:tab-purpose>', views.index)
    #path('recommend/', include('sign.urls')),
    # path('search/', views.SearchFormView.as_view(), name='search'),
]
