"""
노트북 태그 코드
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
from django.db.models import Q
from django.utils import timezone
django.setup()
from note_book_service.models import Prod, Prod_property, Prod_ratings, Tag

class ProdTaging:
    def write_Tag(self):
        Tag(name="#터치스크린").save()
        Tag(name="#팬리스").save()
        Tag(name="#키보드조명").save()
        Tag(name="#숫자키패드").save()
        Tag(name="#초경량").save()
        Tag(name="#가벼운").save()
        Tag(name="#무거운").save()
        Tag(name="#영상편집").save()
        Tag(name="#게이밍").save()
        Tag(name="#사무용").save()
        Tag(name="#웹서핑").save()
        Tag(name="#인강").save()

    def get_add_tag(self, id, spec):
        if not spec.filter(Q(option_id__exact=1) & Q(option_Content__contains="미포함")).exists():
            os_prod = spec.filter(option_id__exact=1).values('option_Content')
            os_prod = list(os_prod.get(option_id__exact=1).values())[0].replace(' ', '')
            os_prod = "#" + os_prod
            try:
                self.TagAdd(id, os_prod)
            except:
                Tag(name=os_prod).save()
                self.TagAdd(id, os_prod)
            print(os_prod)

        if spec.filter(Q(option_id=2) & Q(option_Content="터치화면")).exists():
            self.TagAdd(id, "#터치스크린")
            print("#터치스크린")
        if spec.filter(Q(option_id=10) & Q(option_Content="팬리스(무소음)")).exists():
            self.TagAdd(id, "#팬리스")
        if spec.filter(Q(option_id=10) & Q(option_Content="USB-PD")).exists():
            self.TagAdd(id, "#USB-PD")
            print("#USB-PD")
        if spec.filter(Q(option_id=10) & Q(option_Content="키보드라이트")).exists():
            self.TagAdd(id, "#키보드조명")
            print("#키보드조명")
        if spec.filter(Q(option_id=10) & Q(option_Content="숫자키패드")).exists():
            self.TagAdd(id, "#숫자키패드")
            print("#숫자키패드")

        # now = timezone.now()
        # kst = now.strftime('20%y.%m')
        # print(kst)
        # "#오래된"

    def get_Weight_Tag(self, id, spec):
        wt = spec.filter(option_id=9).values('option_Content')
        wt = list(wt.get(option_title__exact='wt').values())[0]

        wt = float(wt.replace('kg', ''))
        if wt <= 1:
            self.TagAdd(id, "#초경량")
            print("초경량")
        elif wt <= 1.5:
            self.TagAdd(id, "#가벼운")
            print("#가벼운")
        elif wt >= 2.1:
            self.TagAdd(id, "#무거운")
            print("#무거운")

    def get_Purpose_Tag(self, id, spec, ratings):
        scr_Data = ratings.filter(prod_id=id)

        if scr_Data.filter(Q(cpu__gte=3) & Q(gpu__gte=3) & Q(disp__gte=4)):
            self.TagAdd(id, "#영상편집")
        if scr_Data.filter(Q(cpu__gte=2.5) & Q(gpu__gte=3)):
            self.TagAdd(id, "#게이밍")
            print("#게이밍")
        elif scr_Data.filter(Q(cpu__gte=2.5) & Q(gpu__gte=1)):
            self.TagAdd(id, "#사무용")
            print("#사무용")
        elif scr_Data.filter(Q(cpu__gte=1) & Q(gpu__gte=1) & Q(price__gte=4.5)):
            self.TagAdd(id, "#인강")
            print("#웹서핑, #인강")

    def TagAdd(self, id, tag_name):
        id_prod = Prod.objects.get(prod_id=id)
        tag = Tag.objects.get(name=tag_name)
        id_prod.tags.add(tag)

    def StartTag(self):
        list_id_prod = Prod.objects.values('prod_id')
        list_spec_prod = Prod_property.objects.all()
        list_ratings_prod = Prod_ratings.objects.all()

        for id_prod in list_id_prod:
            apple_list = [91571168, 91571201, 91571223, 91571229, 91571234, 91571238, 91571244, 91571252, 91571276,
                          91571299, 91571316, 91571328, 96329901, 96330001, 98764197, ]
            id = int(id_prod.get('prod_id'))
            spec = list_spec_prod.filter(prod_id__exact=id)

            print("=======================", id, "===========================")
            print(Prod.objects.get(prod_id=id), "\n")

            try:
                a1 = Prod.objects.get(prod_id=id)
                a1.tags.get(prod=id)
                print("Check_prod : TRUE") # DB 데이터 유무 확인
            except:
                if id not in apple_list:
                    self.get_Purpose_Tag(id, spec, list_ratings_prod)
                    self.get_Weight_Tag(id, spec)
                    self.get_add_tag(id, spec)
            print("=========================================================\n")

if __name__ == '__main__':
    # Tag(name="#터치스크린").save()
    # Tag(name="#팬리스").save()
    # Tag(name="#키보드조명").save()
    # Tag(name="#숫자키패드").save()
    # Tag(name="#초경량").save()
    # Tag(name="#가벼운").save()
    # Tag(name="#무거운").save()
    # Tag(name="#영상편집").save()
    # Tag(name="#게이밍").save()
    # Tag(name="#사무용").save()
    # Tag(name="#웹서핑").save()
    # Tag(name="#인강").save()
    # Tag(name="#USB-PD").save()


    result = ProdTaging()
    result.StartTag()
    print("작업 완료")
