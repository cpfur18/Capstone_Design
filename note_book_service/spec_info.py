# ==========================================================
"""
상품 정보 페이지 데이터 return 모듈
"""
# ==========================================================
#Django import
import os

#프로젝트 절대경로
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# 웹프레임워크
import django
from django.db.models import Q, F, Sum, Count, Case, When
django.setup()
from note_book_service.models import Prod, Prod_property

class CpuInfo:
    # CPU 기본 정보 set
    def setOptionID(self, prdinf, option_id):
        return prdinf.filter(option_id=option_id)
    def setCpuInfo(self, cpu_ID, title, content):
        return cpu_ID.filter(Q(option_title__contains=title) & Q(option_Content__contains=content)).exists()

    # CPU 상세 성능 get
    def getCpuGen(self, prdinf):
        cpu_gen = prdinf.filter(option_title__contains='c_gen').values('option_Content')
        cpu_gen = cpu_gen.get()
        return list(cpu_gen.values())[0]
    def getCpuName(self, prdinf):
        cpu_name = prdinf.filter(option_title__contains='c_name').values('option_Content')
        cpu_name = cpu_name.get()
        return list(cpu_name.values())[0]
    def getCpuSpeed(self, prdinf):
        cpu_speed = []

        cpu_low_speed = prdinf.filter(option_title__contains='c_low_speed').values('option_Content')
        cpu_low_speed = cpu_low_speed.get()
        cpu_speed.append(list(cpu_low_speed.values())[0])

        cpu_top_speed = prdinf.filter(option_title__contains='c_top_speed').values('option_Content')
        cpu_top_speed = cpu_top_speed.get()
        cpu_speed.append(list(cpu_top_speed.values())[0])

        return cpu_speed
    def getCpuUint(self, prdinf):
        cpu_unit = prdinf.filter(option_title__contains='c_unit').values('option_Content')
        cpu_unit = cpu_unit.get()
        cpu_unit = list(cpu_unit.values())[0]

        if '(' in cpu_unit:
            cpu_unit = cpu_unit.split('(')[0]
        return cpu_unit

    def isCpuCo(self, prdinf):
        cpu_ID = self.setOptionID(prdinf, 3)
        cpu_content = cpu_ID.filter(Q(option_title__contains='c_co') & Q(option_Content__contains='인텔')).exists()

        return cpu_content

    # def CpuSpeedInf(self):

    def setProdCpu(self, prdinf):
        cpu_co = self.isCpuCo(prdinf)
        cpu_speed = self.getCpuSpeed(prdinf)

        # 인텔 CPU
        if cpu_co:
            context = {'cpu_co': '인텔',
                       'cpu_gen': self.getCpuGen(prdinf),
                       'cpu_unit': self.getCpuUint(prdinf),
                       'cpu_name': self.getCpuName(prdinf),
                       'cpu_low_speed': cpu_speed[0],
                       'cpu_top_speed': cpu_speed[1]
                       }

            cpu_smp_exp = context['cpu_co'] + "의 " + "" + "성능을 가진 " + context['cpu_unit'] + " CPU 입니다."

        # AMD CPU
        else:
            context = {'cpu_co': 'AMD',
                       'cpu_gen': self.getCpuGen(prdinf),
                       'cpu_unit': self.getCpuUint(prdinf),
                       'cpu_name': self.getCpuName(prdinf),
                       'cpu_low_speed': cpu_speed[0],
                       'cpu_top_speed': cpu_speed[1]
                       }
            cpu_smp_exp = context['cpu_co'] + "의 " + "" + "성능을 가진 " + context['cpu_unit'] + " CPU 입니다."

        print(cpu_smp_exp)
        return context


class ProdSpecInfo(CpuInfo):
    def makeProdInfo(self, prod_id):
        property = Prod_property
        prdinf = property.objects.filter(prod_id=prod_id)

        cpu_info = self.setProdCpu(prdinf)
        print(cpu_info)



        # gpu_info = ProdSpecInfo().setProdGpu(prdinf)
        # add_info = ProdSpecInfo().setAddOption(prdinf)



        # print(result)
    # def setProdGpu(self, prdinf):
    #
    #
    # def setAddOption(self, prdinf):





info = ProdSpecInfo()
info.makeProdInfo(94001763)

# class