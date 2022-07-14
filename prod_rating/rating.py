#Django import
import os
import sys

#프로젝트 절대경로
sys.path.append('D:\Capstone_Design\config')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# 웹프레임워크
import django
django.setup()
from note_book_service.models import Prod, Prod_property, Passmark_cpu_info, Passmark_gpu_info

# cpu_intel = ['셀러론-6305', '셀러론-N4500', '셀러론-N5100', '셀러론-N4020', '펜티엄-7505', '펜티엄-8505',  '펜티엄-G6405U', '펜티엄-N5030', '코어i3-1215U', '코어i3-1115G4', '코어i3-10110U', '코어i5-12500H', '코어i5-1135G7',  '코어i5-1240P', '코어i5-1240P'  ]
# cpu_amd =
prod_list = Prod.objects.all()
prod_spec_list = Prod_property.objects.all()
cpu_mark = Passmark_cpu_info.objects.all()
gpu_mark = Passmark_gpu_info.objects.all()

for id_check in prod_list:
    id_filter = prod_spec_list.filter(prod_id=id_check)
    for option_check in id_filter:
        option_check.filter(prod_property='option_check')
        print(id_check, ':', option_check.prod_property)
for id_check in prod_list:
    id_filter = prod_spec_list.filter(prod_id=id_check).values_list('prod_property', flat=True)
    for option_check in id_filter:
        print(option_check)

#
# class rating:
#     def __init__(self, prod_list, prod_spec_list, cpu_mark, gpu_mark):
#         self.prod_list = Prod.objects.values('prod_id')
#
#
#
#
#     def cpu_rating(self):
#         self.prod_list
#
#
#     def gpu_rating(id):
#
#
#     # 평가 결과 반환
#     result = 0
#     return result
# cpu
# print(model_id, company, name, price, reg_date)
#
# fk_prod = Prod.objects.get(prod_id=model_id)
# Prod(prod_id=model_id, prod_company=company, prod_name=name, prod_price=price, prod_reg_date=reg_date).save()
#
