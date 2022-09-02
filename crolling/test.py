"""
옵션 크롤링 코드
"""

#Django import
import os
import sys
import re

#프로젝트 절대경로
sys.path.append('C:\Capstone_Design\config')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# 웹프레임워크
import django
django.setup()
from django.db.models import Q
from note_book_service.models import Prod, Prod_property, Prod_ratings, Passmark_cpu_info, Passmark_gpu_info, Prod_Tag, Tag
# Prod_property(prod_id=fk_prod, option_id=option_id, option_title=option_title, option_Content=option_content).save()
# Prod_Tag(Prod.objects.get(prod_id=84819117), Tag.objects.filter(name__exact="#팬리스")).save()

# a1 = Prod.objects.all().values_list()
# print(a1)
# m1 = Tag.objects.get(name="#게이밍")
# print(a1.tags.values())

a1 = Prod.objects.get(prod_id=84819117)
# print(a1)
m1 = Tag.objects.get(name="#게이밍")
# print(a1.tags.all())
# prod_tag.tag.Prod_set.all()
# new_Prod_list = Prod.objects.order_by('-prod_id')[0:5]
# Prod_Tag.objects.all()


# a1 = Tag.objects.get(name='#팬리스')
# a1.Prod_set.all()
# print(Prod_Tag.objects.tags.all())
# for prod_list in new_Prod_list:
#     a = prod_list.tags.values('prod', 'name')
#     print(a)



#
# if purpose == "영상편집":
#     print()
# elif purpose == "게임":
#     print()
# elif purpose == "사무용":
#     print()
# else:
#     print()
ratings = Prod_ratings.objects.all()
prod_id = ratings.filter(Q(cpu__gte=3) & Q(gpu__gte=3) & Q(disp__gte=4))
print(prod_id.values('prod_id'))
