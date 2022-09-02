"""
추천 코드
"""

#Django import
import os
import sys

#프로젝트 절대경로
sys.path.append('C:\Capstone_Design\config')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# 웹프레임워크
import django
from django.db.models import Q, F, Sum, Count, Case, When
django.setup()
from note_book_service.models import Prod, Prod_property, Prod_ratings, Passmark_cpu_info, Passmark_gpu_info

class recr_123:
    def check_purpose(self, purpose):
        ratings = Prod_ratings.objects.all()
        if purpose == "영상편집":
            prod_id = ratings.filter(Q(cpu__gte=3) & Q(gpu__gte=3) & Q(disp__gte=4))
            print("영상편집")
        elif purpose == "게임":
            prod_id = ratings.filter(Q(cpu__gte=2.5) & Q(gpu__gte=3))
            print("게임")
        elif purpose == "사무용":
            prod_id = ratings.filter(Q(cpu__gte=2.5) & Q(gpu__gte=1))
            print("사무용")
        else:
            prod_id = ratings.filter(Q(cpu__gte=1) & Q(gpu__gte=1) & Q(price__gte=4.5))
            print("#웹서핑, #인강")
        return prod_id.values('prod_id')

    def check_price(self, id, price):
        id.values('prod_id')
        ratings = Prod_ratings.objects.filter(prod_id_id__in=id.values('prod_id'))
        if price == "price_1": # 60만
            id = ratings.filter(price=5)
            print(5)
        elif price == "price_2": # 60 ~ 100만원
            id = ratings.filter(price=4)
            print(4)
        elif price == "price_3": # 100 ~ 150만원
            id = ratings.filter(price=3.5)
            print(3.5)
        elif price == "price_4": # 150 ~ 200만원
            id = ratings.filter(price=3)
            print(3)
        elif price == "price_5": # 250만원 반대로
            id = ratings.filter(price__lte=2.5)
            print(2.5, "아래")
        return id

    # def check_weight(self, id, wt):
    #     spec = Prod_property.objects.fliter(prod_id__in=id)
    #     wt = float(wt.replace('kg', ''))
    #     if wt == "wt_5":  # 1kg
    #         id = ratings.fliter(price=5)
    #         print()
    #     elif wt == "wt_4":  # 1.5kg
    #         id = ratings.fliter(price=5)
    #         print()
    #     elif wt == "wt_3":  # 1.8kg
    #         id = ratings.fliter(price=5)
    #         print()
    #     elif wt == "wt_2":  # 2.3kg~
    #         id = ratings.fliter(price=5)
    #         print()
    #     else:
    #         id = ratings.fliter(price=5)
    #         print()

    def check_as(self, id, a):
        if a == "AS_true":
            id = Prod.objects.filter(prod_id__in=id)
            id = id.filter(Q(prod_company="삼성") | Q(prod_company="LG"))
        return id

    def check_disp_size(self, id, size):
        ratings = Prod_ratings.objects.filter(prod_id_id__in=id.values('prod_id'))
        if size == "disp_size_1":
            id = ratings.filter(disp_size=1)
        elif size == "disp_size_2":
            id = ratings.filter(disp_size=2)
        elif size == "disp_size_3":
            id = ratings.filter(Q(disp_size=2.5) | Q(disp_size=3))
        elif size == "disp_size_4":
            id = ratings.filter(disp_size=4)
        else:
            id = ratings.filter(disp_size=5)
        return id

    def check_disp_color(self, id, color):
        ratings = Prod_ratings.objects.filter(prod_id_id__in=id.values('prod_id'))
        if color == "disp_color_true":
            id = ratings.filter(disp__gte=4)
        return id

# recr_123().check_purpose(123123)

