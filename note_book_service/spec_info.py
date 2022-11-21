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
        result = [None, None]
        if '인텔' in cpu_co:
            if 'i3' in c_name:
                result[0] = "보급형"
                result[1] = "문서 작성을 위한 사무용, 동영상 감상, 간단한 게임용으로 사용할 시 적합합니다."
            elif 'i5' in c_name:
                result[0] = "중급형"
                result[1] = "가장 많이 사용하는 등급의 CPU로 중사양 게임, 이미지 편집 등 대부분의 작업 시 적합합니다."
            elif 'i7' in c_name:
                result[0] = "고급형"
                result[1] = "고사양 게임, 동영상 편집 등 고성능이 필요한 작업을 하는 고급 사용자에게 적합합니다."
            elif 'i9' in c_name:
                result[0] = "최고성능"
                result[1] = "최고성능의 CPU로 높은 수준의 작업이 지속적으로 이루어져야하는 사용자에게 적합합니다."
            else:
                result[0] = "저가형"
                result[1] = "문서 작성을 위한 사무용, 웹서핑, 동영상 감상의 용도로 사용할 시 적합합니다."
        else:
            if 'Ryzen 3' in c_name:
                result[0] = "보급형"
                result[1] = "문서 작성을 위한 사무용, 동영상 감상, 간단한 게임용으로 사용할 시 적합합니다."
            elif 'Ryzen 5' in c_name:
                result[0] = "중급형"
                result[1] = "가장 많이 사용하는 등급의 CPU로 중사양 게임, 이미지 편집 등 대부분의 작업 시 적합합니다."
            elif 'Ryzen 7' in c_name:
                result[0] = "고급형"
                result[1] = "고사양 게임, 동영상 편집 등 고성능이 필요한 작업을 하는 고급 사용자에게 적합합니다."
            elif 'Ryzen 9' in c_name:
                result[0] = "최고성능"
                result[1] = "최고성능의 CPU로 높은 수준의 작업이 지속적으로 이루어져야하는 사용자에게 적합합니다."
            else:
                result[0] = "저가형"
                result[1] = "문서 작성을 위한 사무용, 웹서핑, 동영상 감상의 용도로 사용할 시 적합합니다."
        return result

    def getCpuCls(self, c_co, c_name):
        # HX, HK, H, G7, G4, P, U
        c_cls = [None, None]
        cls = c_name.strip()[-2] + c_name.strip()[-1]

        if "인텔" in c_co:
            if "HX" in cls:
                c_cls[0] = "HX"
                c_cls[1] = "인텔의 최고성능 모바일 CPU로 게이밍 노트북에 사용됩니다."
            elif "HK" in cls:
                c_cls[0] = "HK"
                c_cls[1] = "오버클럭이 적용된 고성능 모바일 CPU 모델이며 게이밍 노트북에 주로 사용됩니다."
            elif "H" in cls:
                c_cls[0] = "H"
                c_cls[1] = "고성능 CPU를 의미하며 게이밍 노트북이나 작업용 노트북에 주로 사용됩니다."
            elif "G7" in cls:
                c_cls[0] = "G7"
                c_cls[1] = "G7, G4, G1은 CPU의 내장 그래픽 카드 성능을 의미하며 숫자가 높을수록 성능이 높습니다."
            elif "G4" in cls:
                c_cls[0] = "G4"
                c_cls[1] = "G7, G4, G1은 CPU의 내장 그래픽 카드 성능을 의미하며 숫자가 높을수록 성능이 높습니다."
            elif "G1" in cls:
                c_cls[0] = "G1"
                c_cls[1] = "G7, G4, G1은 CPU의 내장 그래픽 카드 성능을 의미하며 숫자가 높을수록 성능이 높습니다."
            elif "U" in cls:
                c_cls[0] = "U"
                c_cls[1] = "저전력 CPU를 의미하며 전력 효율과 발열에 강점을 가집니다.."
            elif "P" in cls:
                c_cls[0] = "P"
                c_cls[1] = "고성능과 저전력의 중간 벨런스가 잡힌 CPU를 의미합니다."
        else:
            # HX, HS, H, U
            if "HX" in cls:
                c_cls[0] = "HX"
                c_cls[1] = "오버클럭이 적용된 고성능 모바일 CPU 모델이며 게이밍 노트북에 주로 사용됩니다."
            elif "HK" in cls:
                c_cls[0] = "HS"
                c_cls[1] = "고성능과 저전력의 중간 벨런스가 잡힌 CPU를 의미합니다."
            elif "H" in cls:
                c_cls[0] = "H"
                c_cls[1] = "고성능 CPU를 의미하며 게이밍 노트북이나 작업용 노트북에 주로 사용됩니다."
            elif "U" in cls:
                c_cls[0] = "U"
                c_cls[1] = "저전력 CPU를 의미하며 전력 효율과 발열에 강점을 가집니다.."
        return c_cls


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
                   'cpu_top_speed': cpu_speed[1],
                   'cpu_cls': None,
                   'cpu_cls_smp': None,
                   'cpu_smp_exp': None
                   }

        # 인텔 CPU
        if cpu_co:
            context['cpu_co'] = '인텔'
            cpu_cls = self.getCpuCls(context['cpu_co'], context['cpu_name'])
            cpu_lineup = self.getCpuLineUp(context['cpu_co'], context['cpu_name'])
            context['cpu_cls'] = cpu_cls[0]
            context['cpu_cls_smp'] = cpu_cls[1]
            context['cpu_smp_exp'] = context['cpu_co'] + "의 " + cpu_lineup[0] + " CPU로 " + cpu_lineup[1]
        # AMD CPU
        else:
            context['cpu_co'] = 'AMD'
            cpu_cls = self.getCpuCls(context['cpu_co'], context['cpu_name'])
            cpu_lineup = self.getCpuLineUp(context['cpu_co'], context['cpu_name'])
            context['cpu_cls'] = cpu_cls[0]
            context['cpu_cls_smp'] = cpu_cls[1]
            context['cpu_smp_exp'] = context['cpu_co'] + "의 " + cpu_lineup[0] + cpu_lineup[1] + " CPU 입니다."
        return context

class GpuInfo(OptionId):
    # GPU 상세 성능 get
    def getGpuName(self, prdinf):
        gpu_name = prdinf.filter(option_title__contains='g_name').values('option_Content')
        gpu_name = gpu_name.get()
        return list(gpu_name.values())[0]

    def getGpuRam(self, prdinf):
        cpu_low_speed = prdinf.filter(option_title__contains='c_low_speed').values('option_Content')
        cpu_low_speed = cpu_low_speed.get()

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

    def setProdGpu(self, prdinf):
        context = {'gpu_exter': None,
                   'gpu_co': None,
                   'gpu_name': None,
                   'gpu_ram': None,
                   'gpu_ram_exp': None,
                   'gpu_smp_exp': None
                   }

        if self.isGpuVga(prdinf):
            print("외장 그래픽이 있습니다.")
            print(self.getGpuName(prdinf))
            context['gpu_exter'] = 1
            context['gpu_co'] = "NVIDIA"
            context['gpu_name'] = self.getGpuName(prdinf)
            context['gpu_ram'] = self.getGpuRam(prdinf)
            context['gpu_ram_exp'] = self.getGpuRam(prdinf)
            context['gpu_smp_exp'] = self.getGpuRam(prdinf)


            gpu_smp_exp = context['cpu_co'] + "의 " + self.getGpuLineUp(context['cpu_co'], context['cpu_name']) + " " + context['cpu_unit'] + " CPU 입니다."

        else:
            print("내장 그래픽만 존재합니다.")
            context['gpu_name'] = self.getGpuName(prdinf)
            gpu_smp_exp = context['cpu_co'] + "의 " + self.getGpuLineUp(context['cpu_co'], context['cpu_name']) + " " + context['cpu_unit'] + " CPU 입니다."


        return context

# class AddInfo(OptionId):
#     asd


# class ProdSpecInfo(CpuInfo, GpuInfo):
class ProdSpecInfo(CpuInfo):
    def makeProdInfo(self, prod_id):
        property = Prod_property
        prdinf = property.objects.filter(prod_id=prod_id)

        cpu_info = self.setProdCpu(prdinf)
        print(cpu_info)
        # add_info = ProdSpecInfo().setAddOption(prdinf)

info = ProdSpecInfo()
info.makeProdInfo(94001763)

# info.makeProdInfo(92078987)
# class