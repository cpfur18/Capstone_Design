"""
옵션 크롤링 코드
"""

#Django import
import os
import sys

#프로젝트 절대경로
sys.path.append('D:\Capstone_Design\config')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# 웹프레임워크
import django
django.setup()
from note_book_service.models import Prod, Prod_property, Prod_img
import time

# Json 크롤링
import json
import urllib.request as req

os_option = [130659]
display_option = [130702, 219017, 130703, 210408, 130705, 130704, 130709, 130701, 130699, 130696, 215469,
                  212910, 216363, 217080, 217079, 217078]
# DCI-P3 217081 specTitle로 찾아야함
apple_cpu_option = [217166, 211238]
intel_cpu_option = [130715, 214886, 130713, 130726, 211238, 211239, 130733, 130727, 130717, 130729]
amd_cpu_option = [130715, 130713, 212862, 211238, 211239, 130733]
gpu_option = [130614, 214673]
ext_gpu_option = ["그래픽(NVIDIA)", "그래픽(AMD)", 218699, 130628, 130626]
ram_option = [130643, 210963]
stge_option = [130680, 210951]
battery_option = [213912, 130647]
weight_option = [130641, 130644]
add_option = [192356, 130633, 130683, 130687, 130658, 130640, 217044, 130651, 130663, 217083, 213912, 130647,
              217085,130635, 130674, 130645]
class enuri:
    # DB 저장 함수
    def save_desc(self, fk_prod, option_code, specContent):
        Prod_property(prod_id=fk_prod, option_id=option_code, option_title=specContent).save()

    def check_desc(self, dict_spec, fk_prod):
        id_dict = dict_spec.get("att_id")
        specGroupname_id_dict = dict_spec.get("specGroupname")
        specContent_dict = dict_spec.get("specContent")
        specTitle_dict = dict_spec.get("specTitle")

        if id_dict in os_option:
            # print("운영체제 : " + specContent_dict)
            self.save_desc(fk_prod, 1, specContent_dict)
        elif id_dict in display_option:
            # print("Display : " + specContent_dict)
            self.save_desc(fk_prod, 2, specContent_dict)
        elif id_dict == 217081:
            # print("Display : " + "DCI-P3")
            self.save_desc(fk_prod, 2, specTitle_dict)
        elif id_dict in apple_cpu_option:
            # print("CPU : " + specContent_dict)
            self.save_desc(fk_prod, 3, specContent_dict)
        elif id_dict in intel_cpu_option:
            # print("CPU : " + specContent_dict)
            self.save_desc(fk_prod, 3, specContent_dict)
        elif id_dict in amd_cpu_option:
            # print("CPU : " + specContent_dict)
            self.save_desc(fk_prod, 3, specContent_dict)
        elif id_dict in gpu_option:
            # print("내장 그래픽 : " + specContent_dict)
            self.save_desc(fk_prod, 4, specContent_dict)
        elif specGroupname_id_dict in ext_gpu_option:
            # print("외장 그래픽 : " + specContent_dict)
            self.save_desc(fk_prod, 5, specContent_dict)
        elif id_dict in ext_gpu_option:
            # print("외장 그래픽 : " + specContent_dict)
            self.save_desc(fk_prod, 5, specContent_dict)
        elif id_dict in ram_option:
            # print("RAM : " + specContent_dict)
            self.save_desc(fk_prod, 6, specContent_dict)
        elif id_dict in stge_option:
            # print("Storage : " + specContent_dict)
            self.save_desc(fk_prod, 7, specContent_dict)
        elif id_dict in battery_option:
            # print("Battery : " + specContent_dict)
            self.save_desc(fk_prod, 8, specContent_dict)
        elif id_dict in weight_option:
            # print("Weight : " + specContent_dict)
            self.save_desc(fk_prod, 9, specContent_dict)
        elif id_dict in add_option:
            # print("ADD : " + specContent_dict)
            self.save_desc(fk_prod, 10, specContent_dict)
        else:
            pass


    # ============================ 상품 옵션 DB저장=============================================
    def prodDesc(self):
        list_prod = Prod.objects.values('prod_id')
        list_spec_prod = Prod_property.objects.distinct().values('prod_id')

        for id_prod in list_prod:
            id = str(id_prod.get('prod_id'))
            try:
                list_spec_prod.get(prod_id=id)
                print("Check_prod : TRUE")
            except:
                print("Check_prod : FALSE")
                url = "http://www.enuri.com/wide/api/product/prodDesc.jsp?type=S&modelno=" + id
                res = req.urlopen(url)
                json_obj = json.load(res)
                print("http://www.enuri.com/wide/api/product/prodDesc.jsp?type=S&modelno=" + id)
                fk_prod = Prod.objects.get(prod_id=id)
                print(fk_prod)
                for list_spec in json_obj['enuri_spec_table']:
                    self.check_desc(list_spec, fk_prod)
                print("DB 저장 완료")
                print("\n")

    # ===================================================================================
if __name__ == '__main__':
    result = enuri()
    result.prodDesc()
    print("크롤링이 완료되었습니다.")