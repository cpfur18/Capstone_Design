"""
옵션 크롤링 코드
"""

#Django import
import os
import sys

#프로젝트 절대경로
sys.path.append('C:\Capstone_Design\config')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# 웹프레임워크
import django
django.setup()
from note_book_service.models import Prod, Prod_property, Prod_ratings, Passmark_cpu_info, Passmark_gpu_info
import time

class Get_score_Prod:
    # ======================= 처리 성능 =============================
    def cpu_score(self, spec_prod, mark_cpu_prod):
        getNameCpu = spec_prod.filter(option_title__icontains='c_name').values('option_Content')
        cent_cpu = 36322 / 100
        try:
            getMarkCpu = mark_cpu_prod.filter(cpu_name__icontains=getNameCpu).values('cpu_mark')
            getMarkCpu = getMarkCpu.get()
            getMarkCpu = list(getMarkCpu.values())
            print("벤치마크 점수 :", getMarkCpu[0])
            mark = int(round(getMarkCpu[0] / cent_cpu, 0))
            print("퍼센트 : ", mark)
            if 0 <= mark <= 10:
                print("1점")
            elif 11 <= mark <= 20:
                print("2점")
            elif 21 <= mark <= 30:
                print("2.5점")
            elif 31 <= mark <= 40:
                print("3점")
            elif 41 <= mark <= 50:
                print("3.5점")
            elif 51 <= mark <= 60:
                print("4점")
            elif 71 <= mark <= 80:
                print("4.5점")
            elif 81 <= mark <= 100:
                print("5점")
        except:
            print("CPU : Error")

    def gpu_score(self):
        getNameGpu = spec_prod.filter(option_title__icontains='g_name').values('option_Content')
        cent_gpu = 36322 / 100
        try:
            getMarkGpu = mark_gpu_prod.filter(cpu_name__icontains=getNameGpu).values('cpu_mark')
            getMarkGpu = getMarkGpu.get()
            getMarkGpu = list(getMarkGpu.values())
            print("벤치마크 점수 :", getMarkCpu[0])
            mark = int(round(getMarkCpu[0] / cent_cpu, 0))
            print("퍼센트 : ", mark)
            if 0 <= mark <= 10:
                print("1점")
            elif 11 <= mark <= 20:
                print("2점")
            elif 21 <= mark <= 30:
                print("2.5점")
            elif 31 <= mark <= 40:
                print("3점")
            elif 41 <= mark <= 50:
                print("3.5점")
            elif 51 <= mark <= 60:
                print("4점")
            elif 71 <= mark <= 80:
                print("4.5점")
            elif 81 <= mark <= 100:
                print("5점")
        except:
            print("CPU : Error")
    def ram_score(self):
        print()
    def stg_score(self):
        print()
    # ==============================================================


    # ========================== 화면 ===============================
    def size_display_score(self):
        print()

    def display_score(self):
        print()
    # ==============================================================


    # ========================== 휴대성 ==============================
    # def gpu_score(self):
    #     print()
    # def price_score(self):
    #     print()
    # def cpu_score(self):
    #     print()
    # def gpu_score(self):
    #     print()
    # def price_score(self):
    #     print()
    # ==============================================================

class StartScore(Get_score_Prod):
    def start(self):
        list_id_prod = Prod.objects.values('prod_id')[0:5]
        list_spec_prod = Prod_property.objects.all()
        mark_cpu_prod = Passmark_cpu_info.objects.all()
        mark_gpu_prod = Passmark_gpu_info.objects.all()
        list_ratings_prod = Prod_ratings.objects.all()

        for id_prod in list_id_prod:
            id = str(id_prod.get('prod_id'))
            spec_prod = list_spec_prod.filter(prod_id__exact=id)

            try:
                list_ratings_prod.get(prod_id=id)
                print("Check_prod : TRUE")
            except:
                print("Check_prod : FALSE")
                self.cpu_score(spec_prod, mark_cpu_prod)
                self.gpu_score(spec_prod, mark_gpu_prod)


            # try:
            #     list_spec_prod = Prod_property.objects.filter(prod_id__in=id)
            #
            # except:
            #     print("DB Error")

if __name__ == '__main__':
    result = StartScore()
    result.start()
    print("스코어링 완료")
#
# list_id_prod = Prod.objects.all()
# list_spec_prod = Prod_property.objects.filter(prod_id__in=list_id_prod.values('prod_id'))
# list_spec_prod = Prod_property.objects.filter(prod_id__exact=56068060)
# cpu_spec_prod = list_spec_prod.filter(option_title__exact='c_name')
# mark_cpu_prod = Passmark_cpu_info.objects.filter(cpu_name__icontains=cpu_spec_prod.values('option_Content'))
#
# print(mark_cpu_prod.values())
