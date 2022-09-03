import os
import sys

# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from django.shortcuts import render
from datetime import datetime
from django.utils import timezone
from django.http import HttpResponse
from django.core import serializers
from board.models import Post
from .models import Prod, Prod_property, Prod_ratings
from . import check_recr
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def index(request):
    # 현 시각 Year, month
    # now = timezone.now()
    # kst = now.strftime('%y.%m')

    page = request.GET.get('page', '1')  # 페이지

    # new_Prod_list = Prod.objects.order_by('-prod_id')[0:5]
    Prod_id_list = Prod.objects.order_by('-prod_id')

    paginator = Paginator(Prod_id_list, 5)  # 페이지당 5개씩 보여주기
    page_obj = paginator.get_page(page)

    page_count = len(page_obj.object_list)
    print("=========================================================================")
    print(page_obj.object_list)
    spec_tags_1 = None
    spec_tags_2 = None
    spec_tags_3 = None
    spec_tags_4 = None
    spec_tags_5 = None
    print("=========================================================================")
    if page_count >= 1:
        spec_tags_1 = page_obj.object_list[0].tags.values('prod', 'name')
    if page_count >= 2:
        spec_tags_2 = page_obj.object_list[1].tags.values('prod', 'name')
    if page_count >= 3:
        spec_tags_3 = page_obj.object_list[2].tags.values('prod', 'name')
    if page_count >= 4:
        spec_tags_4 = page_obj.object_list[3].tags.values('prod', 'name')
    if page_count == 5:
        spec_tags_5 = page_obj.object_list[4].tags.values('prod', 'name')

    context = {'Prod_list': page_obj,
               'spec_tags_1': spec_tags_1,
               'spec_tags_2': spec_tags_2,
               'spec_tags_3': spec_tags_3,
               'spec_tags_4': spec_tags_4,
               'spec_tags_5': spec_tags_5,
               }
    return render(request, 'note_book_service/index.html', context)

def product(request, prod_id):
    Prod_list = Prod.objects.filter(prod_id__contains=prod_id)
    prod_id = Prod.objects.get(prod_id__contains=prod_id)
    ratings = Prod_ratings.objects.filter(prod_id=prod_id)
    # for prod_list in new_Prod_list:

    Prod_tags = prod_id.tags.values()

    Prod_list_spec = Prod_property.objects.filter(prod_id__in=Prod_list.values('prod_id'))

    context = {'Prod_list': Prod_list,
               'Prod_list_spec': Prod_list_spec,
               'Prod_tags': Prod_tags,
               'ratings': ratings
               }
    return render(request, 'note_book_service/product.html', context)

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

def recr(request):
    purpose = request.POST['용도']
    wight = request.POST['휴대성']
    price = request.POST['예산']
    as_ = request.POST['제조사']
    try:
        disp_media = request.POST['영상편집_화질']
    except:
        pass
    disp_color2 = request.POST['디스플레이_색감']
    disp_size = request.POST['디스플레이_크기']

    # print(purpose)
    # print(wight)
    # print(price)
    # print(as_)
    # # print(disp_media)
    # print(disp_color2)
    # print(disp_size)

    recr_2 = check_recr.recr_123()
    id = recr_2.check_purpose(purpose)
    id = recr_2.check_price(id, price)
    # id = recr_2.check_weight(id, wight)
    id = recr_2.check_disp_size(id, disp_size)
    id = recr_2.check_disp_color(id, disp_color2)
    id = recr_2.check_as(id, as_)


    recr_Prod_list = Prod.objects.filter(prod_id__in=id).order_by('-prod_id')
    # recr_Prod_list_spec = Prod_property.objects.filter(prod_id__in=recr_Prod_list).order_by('option_id')
    print(recr_Prod_list)

    paginator = Paginator(recr_Prod_list, 5)  # 페이지당 5개씩 보여주기
    page_obj = paginator.get_page(5)
    # page_obj = paginator.get_page(page)

    page_count = len(page_obj.object_list)
    spec_tags_1 = None
    spec_tags_2 = None
    spec_tags_3 = None
    spec_tags_4 = None
    spec_tags_5 = None

    if page_count >= 1:
        spec_tags_1 = page_obj.object_list[0].tags.values('prod', 'name')
    if page_count >= 2:
        spec_tags_2 = page_obj.object_list[1].tags.values('prod', 'name')
    if page_count >= 3:
        spec_tags_3 = page_obj.object_list[2].tags.values('prod', 'name')
    if page_count >= 4:
        spec_tags_4 = page_obj.object_list[3].tags.values('prod', 'name')
    if page_count == 5:
        spec_tags_5 = page_obj.object_list[4].tags.values('prod', 'name')

    context = {'Prod_list': page_obj,
               'spec_tags_1': spec_tags_1,
               'spec_tags_2': spec_tags_2,
               'spec_tags_3': spec_tags_3,
               'spec_tags_4': spec_tags_4,
               'spec_tags_5': spec_tags_5,
               }
    return render(request, 'note_book_service/rec_result.html', context)
    # return render(request, 'note_book_service/rec_result.html')