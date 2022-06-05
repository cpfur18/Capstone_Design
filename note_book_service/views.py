from django.shortcuts import render
from datetime import datetime
from django.utils import timezone
from django.http import HttpResponse
from .models import Prod, Prod_property

def index(request):
    # 현 시각 Year, month
    now = timezone.now()
    kst = now.strftime('%y.%m')

    best_Prod_list = Prod.objects.filter(prod_reg_date__contains=22.05).order_by('-prod_id')[:5]
    best_Prod_list_spec = Prod_property.objects.filter(prod_id__in=best_Prod_list.values('prod_id'))

    context = {'best_Prod_list' : best_Prod_list,
               'best_Prod_list_spec' : best_Prod_list_spec
               }
    return render(request, 'note_book_service/index.html', context)

