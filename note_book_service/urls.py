from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    # path('search/', views.SearchFormView.as_view(), name='search'),

    path('shop/<prod_id>/', views.shop, name='prod_info'),
    # path('coding/', views),
    # path('video_edit/', views),
    # path('office/', views),

    # path('select-tab/<str:tab-purpose>', views.index)
]
