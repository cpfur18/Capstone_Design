"""
view 보조 코드
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
from django.db.models import Q, F, Sum, Count, Case, When
django.setup()
from note_book_service.models import Prod, Prod_property, Prod_ratings, Passmark_cpu_info, Passmark_gpu_info


class Get_Score_Prod:
    def Core_Seach_Intel(self, mark_cpu_prod, cent_cpu, cpu_name):
        getMarkCpu = mark_cpu_prod.filter(cpu_name__exact='Intel Core ' + cpu_name).values('cpu_mark')
        getMarkCpu = getMarkCpu.get()
        getMarkCpu = list(getMarkCpu.values())
        mark = int(round(getMarkCpu[0] / cent_cpu, 0))
        return mark

    def Ryzen_Seach_Amd(self, mark_cpu_prod, cent_cpu, cpu_name):
        getMarkCpu = mark_cpu_prod.filter(cpu_name__exact='AMD ' + cpu_name).values('cpu_mark')
        getMarkCpu = getMarkCpu.get()
        getMarkCpu = list(getMarkCpu.values())
        mark = int(round(getMarkCpu[0] / cent_cpu, 0))
        return mark

    def seach_ryzen_cpu(self, spec_prod, mark_cpu_prod, cent_cpu, cpu_name):
        getNameCpu = spec_prod.filter(option_title__icontains='c_name').values('option_Content')
        getNameCpu = getNameCpu.get(option_Content=cpu_name)

        if "Ryzen 7 5800H" in list(getNameCpu.values())[0]:
            mark = self.Ryzen_Seach_Amd(mark_cpu_prod, cent_cpu, cpu_name)
        if "Ryzen 9 PRO 6950HS" in list(getNameCpu.values())[0]:
            mark = self.Ryzen_Seach_Amd(mark_cpu_prod, cent_cpu, cpu_name)
        if "Ryzen 9 PRO 6950H" in list(getNameCpu.values())[0]:
            mark = self.Ryzen_Seach_Amd(mark_cpu_prod, cent_cpu, cpu_name)
        if "Ryzen 9 6900HS" in list(getNameCpu.values())[0]:
            mark = self.Ryzen_Seach_Amd(mark_cpu_prod, cent_cpu, cpu_name)
        if "Ryzen 9 6900HX" in list(getNameCpu.values())[0]:
            mark = self.Ryzen_Seach_Amd(mark_cpu_prod, cent_cpu, cpu_name)
        if "Ryzen 9 6900H" in list(getNameCpu.values())[0]:
            mark = self.Ryzen_Seach_Amd(mark_cpu_prod, cent_cpu, cpu_name)
        if "Ryzen 7 PRO 6850HS" in list(getNameCpu.values())[0]:
            mark = self.Ryzen_Seach_Amd(mark_cpu_prod, cent_cpu, cpu_name)
        if "Ryzen 7 PRO 6850H" in list(getNameCpu.values())[0]:
            mark = self.Ryzen_Seach_Amd(mark_cpu_prod, cent_cpu, cpu_name)
        if "Ryzen 7 6800HS" in list(getNameCpu.values())[0]:
            mark = self.Ryzen_Seach_Amd(mark_cpu_prod, cent_cpu, cpu_name)
        if "Ryzen 7 6800H" in list(getNameCpu.values())[0]:
            mark = self.Ryzen_Seach_Amd(mark_cpu_prod, cent_cpu, cpu_name)
        if "Ryzen 5 6600HS" in list(getNameCpu.values())[0]:
            mark = self.Ryzen_Seach_Amd(mark_cpu_prod, cent_cpu, cpu_name)
        if "Ryzen 5 6600H" in list(getNameCpu.values())[0]:
            mark = self.Ryzen_Seach_Amd(mark_cpu_prod, cent_cpu, cpu_name)
        if "Ryzen 5 4600H" in list(getNameCpu.values())[0]:
            mark = self.Ryzen_Seach_Amd(mark_cpu_prod, cent_cpu, cpu_name)

        if "i7-12800HX" in list(getNameCpu.values())[0]:
            mark = self.Core_Seach_Intel(mark_cpu_prod, cent_cpu, cpu_name)
        if "i7-12800H" in list(getNameCpu.values())[0]:
            mark = self.Core_Seach_Intel(mark_cpu_prod, cent_cpu, cpu_name)
        if "i9-12900HK" in list(getNameCpu.values())[0]:
            mark = self.Core_Seach_Intel(mark_cpu_prod, cent_cpu, cpu_name)
        if "i9-12900H" in list(getNameCpu.values())[0]:
            mark = self.Core_Seach_Intel(mark_cpu_prod, cent_cpu, cpu_name)
        if "i7-8565U" in list(getNameCpu.values())[0]:
            mark = self.Core_Seach_Intel(mark_cpu_prod, cent_cpu, cpu_name)
        return mark

    # ======================= 처리 성능 =============================
    def getCpuScore(self, spec_prod, mark_cpu_prod):
        cent_cpu = 36723 / 100
        getNameCpu = spec_prod.filter(option_title__icontains='c_name').values('option_Content')
        NameCpu = list(getNameCpu.get(option_Content__contains=getNameCpu).values())[0]
        print("CPU NAME :", NameCpu)
        # 88227996
        try:
            if "Ryzen 7 5800H" in NameCpu:
                mark = self.seach_ryzen_cpu(spec_prod, mark_cpu_prod, cent_cpu, "Ryzen 7 5800H")
            elif "Ryzen 9 PRO 6950HS" in NameCpu:
                mark = self.seach_ryzen_cpu(spec_prod, mark_cpu_prod, cent_cpu, "Ryzen 9 PRO 6950HS")
            elif "Ryzen 9 PRO 6950H" in NameCpu:
                mark = self.seach_ryzen_cpu(spec_prod, mark_cpu_prod, cent_cpu, "Ryzen 9 PRO 6950H")
            elif "Ryzen 9 6900HS" in NameCpu:
                mark = self.seach_ryzen_cpu(spec_prod, mark_cpu_prod, cent_cpu, "Ryzen 9 6900HS")
            elif "Ryzen 9 6900HX" in NameCpu:
                mark = self.seach_ryzen_cpu(spec_prod, mark_cpu_prod, cent_cpu, "Ryzen 9 6900HX")
            elif "Ryzen 9 6900H" in NameCpu:
                mark = self.seach_ryzen_cpu(spec_prod, mark_cpu_prod, cent_cpu, "Ryzen 9 6900H")
            elif "Ryzen 7 PRO 6850HS" in NameCpu:
                mark = self.seach_ryzen_cpu(spec_prod, mark_cpu_prod, cent_cpu, "Ryzen 7 PRO 6850HS")
            elif "Ryzen 7 PRO 6850H" in NameCpu:
                mark = self.seach_ryzen_cpu(spec_prod, mark_cpu_prod, cent_cpu, "Ryzen 7 PRO 6850H")
            elif "Ryzen 7 6800HS" in NameCpu:
                mark = self.seach_ryzen_cpu(spec_prod, mark_cpu_prod, cent_cpu, "Ryzen 7 6800HS")
            elif "Ryzen 7 6800H" in NameCpu:
                mark = self.seach_ryzen_cpu(spec_prod, mark_cpu_prod, cent_cpu, "Ryzen 7 6800H")
            elif "Ryzen 5 6600HS" in NameCpu:
                mark = self.seach_ryzen_cpu(spec_prod, mark_cpu_prod, cent_cpu, "Ryzen 5 6600HS")
            elif "Ryzen 5 6600H" in NameCpu:
                mark = self.seach_ryzen_cpu(spec_prod, mark_cpu_prod, cent_cpu, "Ryzen 5 6600H")
            elif "Ryzen 5 4600H" in NameCpu:
                mark = self.seach_ryzen_cpu(spec_prod, mark_cpu_prod, cent_cpu, "Ryzen 5 4600H")

            elif "i7-12800HX" in NameCpu:
                mark = self.seach_ryzen_cpu(spec_prod, mark_cpu_prod, cent_cpu, "i7-12800HX")
            elif "i7-12800H" in NameCpu:
                mark = self.seach_ryzen_cpu(spec_prod, mark_cpu_prod, cent_cpu, "i7-12800H")
            elif "i9-12900HK" in NameCpu:
                mark = self.seach_ryzen_cpu(spec_prod, mark_cpu_prod, cent_cpu, "i9-12900HK")
            elif "i9-12900H" in NameCpu:
                mark = self.seach_ryzen_cpu(spec_prod, mark_cpu_prod, cent_cpu, "i9-12900H")
            elif "i7-8565U" in NameCpu:
                mark = self.seach_ryzen_cpu(spec_prod, mark_cpu_prod, cent_cpu, "i7-8565U")

            else:
                getMarkCpu = mark_cpu_prod.filter(cpu_name__icontains=NameCpu).values('cpu_mark')
                getMarkCpu = getMarkCpu.get()
                getMarkCpu = list(getMarkCpu.values())
                mark = int(round(getMarkCpu[0] / cent_cpu, 0))

        except:
            print("CPU : Error")

        return score_cpu

    def start_cpu(self, ):
        cpu_score = self.getCpuScore(spec_prod, mark_cpu_prod)