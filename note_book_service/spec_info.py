# ==========================================================
"""
상품 정보 페이지 데이터 return 모듈
"""
# ==========================================================
# Django import
import os

# 프로젝트 절대경로
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Django set
import django
from django.db.models import Q, F, Sum, Count, Case, When
django.setup()
from note_book_service.models import Prod, Prod_property

class OptionId:
    # Target Prod Set
    def setOptionID(self, prdinf, option_id):
        return prdinf.filter(option_id=option_id)

class CpuInfo(OptionId):
    # CPU spec get
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

    def getCpuLineUp(self, cpu_co, c_name):
        if '인텔' in cpu_co:
            if 'i3' in c_name:
                result = "보급형"
            elif 'i5' in c_name:
                result = "중급형"
            elif 'i7' in c_name:
                result = "고급형"
            elif 'i9' in c_name:
                result = "최고성능"
            else:
                result = "저가형"
        else:
            if 'Ryzen 3' in c_name:
                result = "보급형"
            elif 'Ryzen 5' in c_name:
                result = "중급형"
            elif 'Ryzen 7' in c_name:
                result = "고급형"
            elif 'Ryzen 9' in c_name:
                result = "최고성능"
            else:
                result = "저가형"
        return result

    def isCpuCo(self, prdinf):
        cpu_ID = self.setOptionID(prdinf, 3)
        cpu_content = cpu_ID.filter(Q(option_title__contains='c_co') & Q(option_Content__contains='인텔')).exists()

        return cpu_content

    def setProdCpu(self, prdinf):
        cpu_co = self.isCpuCo(prdinf)
        cpu_speed = self.getCpuSpeed(prdinf)

        context = {'cpu_co': None,
                   'cpu_gen': self.getCpuGen(prdinf),
                   'cpu_unit': self.getCpuUint(prdinf),
                   'cpu_name': self.getCpuName(prdinf),
                   'cpu_low_speed': cpu_speed[0],
                   'cpu_top_speed': cpu_speed[1]
                   }

        # 인텔 CPU
        if cpu_co:
            context['cpu_co'] = '인텔'
            cpu_smp_exp = context['cpu_co'] + "의 " + self.getCpuLineUp(context['cpu_co'], context['cpu_name']) + " " + context['cpu_unit'] + " CPU 입니다."

        # AMD CPU
        else:
            context['cpu_co'] = 'AMD'
            cpu_smp_exp = context['cpu_co'] + "의 " + self.getCpuLineUp(context['cpu_co'], context['cpu_name']) + " " + context['cpu_unit'] + " CPU 입니다."

        return cpu_smp_exp

class GpuInfo(OptionId):
    # GPU 상세 성능 get
    def getGpuName(self, prdinf):
        gpu_name = prdinf.filter(option_title__contains='g_name').values('option_Content')
        gpu_name = gpu_name.get()
        return list(gpu_name.values())[0]

    def getGpuRam(self, prdinf):
        cpu_low_speed = prdinf.filter(option_title__contains='c_low_speed').values('option_Content')
        cpu_low_speed = cpu_low_speed.get()
        cpu_speed.append(list(cpu_low_speed.values())[0])

        cpu_top_speed = prdinf.filter(option_title__contains='c_top_speed').values('option_Content')
        cpu_top_speed = cpu_top_speed.get()
        cpu_speed.append(list(cpu_top_speed.values())[0])

        return cpu_speed

    def getGpuLineUp(self, cpu_co, c_name):
        result = None
        if '인텔' in cpu_co:
            if 'i3' in c_name:
                result = "보급형"
            if 'i5' in c_name:
                result = "중급형"
            if 'i7' in c_name:
                result = "고급형"
            if 'i9' in c_name:
                result = "최고성능"
            else:
                result = "저가형"
        else:
            if 'Ryzen 3' in c_name:
                result = "보급형"
            if 'Ryzen 5' in c_name:
                result = "중급형"
            if 'Ryzen 7' in c_name:
                result = "고급형"
            if 'Ryzen 9' in c_name:
                result = "최고성능"
            else:
                result = "저가형"
        return result

    def isGpuVga(self, prdinf):
        result = self.setOptionID(prdinf, 5).exists()
        return result

    def isGpuCo(self, gpu_name):
        if 'Radeon' in gpu_name:
            result = True
        else:
            result = False
        return result

    def setProdGpu(self, prdinf):
        context = {'gpu_co': None,
                   'gpu_name': None,
                   'gpu_ram': None
                   }

        if self.isGpuVga(prdinf):
            print("외장 그래픽이 있습니다.")
            print(self.getGpuName(prdinf))
            context['gpu_name'] = self.getGpuName(prdinf)
            context['gpu_ram'] = self.getGpuUint(prdinf)

            # Radeon, RTX, GTX, MX, Quadro, TI, Max-Q
            gpu_smp_exp = context['cpu_co'] + "의 " + self.getGpuLineUp(context['cpu_co'], context['cpu_name']) + " " + context['cpu_unit'] + " CPU 입니다."

        else:
            print("내장 그래픽만 존재합니다.")

        return cpu_smp_exp

# class AddInfo(OptionId):
#     asd


class ProdSpecInfo(CpuInfo, GpuInfo):
    def makeProdInfo(self, prod_id):
        property = Prod_property
        prdinf = property.objects.filter(prod_id=prod_id)

        cpu_info = self.setProdCpu(prdinf)
        print(cpu_info)
        gpu_info = self.setProdGpu(prdinf)
        print(gpu_info)
        # add_info = ProdSpecInfo().setAddOption(prdinf)

info = ProdSpecInfo()
info.makeProdInfo(94001763)

# info.makeProdInfo(92078987)
# class