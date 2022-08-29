from django.shortcuts import render
from datetime import datetime
from django.utils import timezone
from django.http import HttpResponse
from django.core import serializers

from board.models import Post
from .models import Prod, Prod_property

def getApi(request):
    property = Prod_property.objects.filter(prod_id__exact=97149727).order_by('option_id')
    property_list = serializers.serialize('json', property)
    return HttpResponse(property_list, content_type="text/json-comment-filtered; charset=utf-8")

def apiTest(request):
    return render(request, 'apiTest.html')

def index(request):
    # 현 시각 Year, month
    # now = timezone.now()
    # kst = now.strftime('%y.%m')

    new_Prod_list = Prod.objects.order_by('-prod_id')[0:5]
    new_Prod_list_spec = Prod_property.objects.filter(prod_id__in=new_Prod_list).order_by('option_id')
    print(len(new_Prod_list_spec.values('prod_id')))

    context = {'Prod_list': new_Prod_list,
               'Prod_list_spec': new_Prod_list_spec,
               }
    return render(request, 'note_book_service/index.html', context)

def expolre(request, prod_id):
    Prod_list = Prod.objects.filter(prod_id__contains=prod_id)
    Prod_list_spec = Prod_property.objects.filter(prod_id__in=Prod_list.values('prod_id'))

    context = {'Prod_list': Prod_list,
               'Prod_list_spec': Prod_list_spec,
               }
    return render(request, 'note_book_service/expolre.html', context)

def cmd(request):
    best_commend = 1
    best_commend_list = 2
    comd = {'best_commend' : best_commend,
            'best_commend_list' : best_commend_list,}
    return render(request, 'note_book_service/recommend.html', comd)

def comm(request):
    posts = Post.objects.all().order_by('-id') #object : ORM에서 사용되는 manage 객체 => all은 모두 가져오는 것. get은 하나.
    context = {'posts':posts}
    return render(request, "note_book_service/community.html", context)
    #return render(request, 'note_book_service/community.html', commu)

def pstif(request):
    best_pstif = 1
    best_pstif_list = 2
    pstt = {'best_pstif' : best_pstif,
            'best_pstif_list' : best_pstif_list,}
    return render(request, 'note_book_service/postinfo.html', pstt)

def wrt(request):
    best_wrt = 1
    best_wrt_list = 2
    wrtt = {'best_wrt' : best_wrt,
            'best_wrt_list' : best_wrt_list,}
    return render(request, 'note_book_service/write.html', wrtt)