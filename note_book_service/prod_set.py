#Django import
import os
import sys

#프로젝트 절대경로
sys.path.append('C:\Capstone_Design\config')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import json

# 웹프레임워크
import django
django.setup()
from note_book_service.models import Prod, Prod_property

class prod_set:
    def seting(self):
        prod = Prod_property.objects.filter(prod_id__exact=97149727).order_by('option_id')
        os = prod.filter(option_id__exact=1).values('option_title')
        print(len(prod))
        print("운영체제 : " + str(os))


if __name__ == '__main__':
    result = prod_set()
    result.seting()