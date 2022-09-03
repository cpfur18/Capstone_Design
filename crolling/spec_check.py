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
from note_book_service.models import Prod, Prod_property
import time

# Json 크롤링
import json
import urllib.request as req

os_option = [130659]
display_option = [130702, 219017, 130703, 210408, 130705, 130704, 130709, 130701, 130699, 130696, 215469,
                  212910, 216363]
Color_display_option = [217080, 217079, 217078]
# DCI-P3 217081 specTitle로 찾아야함
apple_cpu_option = [217166, 211238]
intel_cpu_option = [130715, 214886, 130713, 130726, 211238, 211239, 130733, 130727, 130717, 130729, 130725, 213419,
                    201885]
i_intel_cpu_name = ["코어i3-", "코어i5-", "코어i7-", "코어i9-"]
amd_cpu_option = [130715, 130713, 212862, 211238, 211239, 130733, 130730]
gpu_option = [130614, 214673, 219056]
ext_gpu_option = ["그래픽(NVIDIA)", "그래픽(AMD)", 218699, 130628]
ram_option = [130643, 210963]
stge_option = [130680, 210951, 130678, 216825]
battery_option = [213912, 130647, 130645]
add_option = [192356, 130633, 130683, 130658, 130640, 217044, 130651, 130663, 217083, 213912, 130647,
              217085,130635, 130674]
# 웹캠 전면 specTitle + specContent 130687
class enuri:
    # DB 저장 함수
    def save_desc(self, fk_prod, option_id, option_title, option_content):
        Prod_property(prod_id=fk_prod, option_id=option_id, option_title=option_title, option_Content=option_content).save()

    def check_desc(self, dict_spec, fk_prod):
        id_dict = dict_spec.get("att_id")
        specGroupname_id_dict = dict_spec.get("specGroupname")
        specContent_dict = dict_spec.get("specContent")
        specTitle_dict = dict_spec.get("specTitle")

        if id_dict in os_option:
            self.save_desc(fk_prod, 1, None, specContent_dict)
        # ============================== 디스플레이 =======================================
        elif id_dict in display_option:
            if "인치" in specContent_dict:
                self.save_desc(fk_prod, 2, "d_size", specContent_dict)
            elif id_dict == 130703:
                self.save_desc(fk_prod, 2, "d_res", specContent_dict)
            elif id_dict == 130709:
                self.save_desc(fk_prod, 2, "d_pnl", specContent_dict)
            elif id_dict == 130696:
                self.save_desc(fk_prod, 2, "d_bhp", specContent_dict)
            elif id_dict == 212910:
                self.save_desc(fk_prod, 2, "d_rate", specContent_dict)
            else:
                self.save_desc(fk_prod, 2, None, specContent_dict)
        elif id_dict in Color_display_option:
            if id_dict == 217080:
                self.save_desc(fk_prod, 2, "d_color_argb", specTitle_dict + " " + specContent_dict)
            if id_dict == 217079:
                self.save_desc(fk_prod, 2, "d_color_srgb", specTitle_dict + " " + specContent_dict)
            if id_dict == 217078:
                self.save_desc(fk_prod, 2, "d_color_ntsc", specTitle_dict + " " + specContent_dict)

        elif id_dict == 217081:
            self.save_desc(fk_prod, 2, "d_color_dci", specTitle_dict + " " + specContent_dict)

        # ================================= CPU =========================================
        elif id_dict in apple_cpu_option:
            if id_dict == 211238:
                self.save_desc(fk_prod, 3, "c_unit", specContent_dict)
            elif id_dict == 130715:
                self.save_desc(fk_prod, 3, "c_co", specContent_dict)
            else:
                if "M1" in specContent_dict:
                    specContent_dict = specContent_dict.replace('M1', 'Apple M1')
                elif "M2" in specContent_dict:
                    specContent_dict = specContent_dict.replace('M2', 'Apple M2')
                self.save_desc(fk_prod, 3, "c_name", specContent_dict)

        elif id_dict in intel_cpu_option:
            if any(keyword in specContent_dict for keyword in i_intel_cpu_name):
                specContent_dict = specContent_dict.replace('코어', '')
                if "i3-12세대" in specContent_dict:
                    specContent_dict = specContent_dict.replace('i3-12세대', '코어i3 12세대')
                    self.save_desc(fk_prod, 3, None, specContent_dict)
                else:
                    self.save_desc(fk_prod, 3, "c_name", specContent_dict)
            elif "펜티엄-" in specContent_dict:
                specContent_dict = specContent_dict.replace('펜티엄-', '')
                self.save_desc(fk_prod, 3, "c_name", specContent_dict)
            elif "셀러론-" in specContent_dict:
                specContent_dict = specContent_dict.replace('셀러론-', 'Celeron ')
                self.save_desc(fk_prod, 3, "c_name", specContent_dict)
            elif id_dict == 201885:
                self.save_desc(fk_prod, 3, "c_name", specContent_dict)
            elif id_dict == 130715:
                self.save_desc(fk_prod, 3, "c_co", specContent_dict)
            elif id_dict == 130713:
                self.save_desc(fk_prod, 3, "c_gen", specContent_dict)
            elif id_dict == 211238:
                self.save_desc(fk_prod, 3, "c_unit", specContent_dict)
            elif id_dict == 211239:
                self.save_desc(fk_prod, 3, "c_low_speed", specContent_dict)
            elif id_dict == 130733:
                self.save_desc(fk_prod, 3, "c_top_speed", specContent_dict)
            elif "확인 후 구매" in specContent_dict:
                self.save_desc(fk_prod, 3, 'c_name', '직접확인')
            else:
                self.save_desc(fk_prod, 3, None, specContent_dict)

        elif id_dict in amd_cpu_option:
            if "라이젠" in specContent_dict:
                specContent_dict = specContent_dict.replace('라이젠', 'Ryzen ')
                specContent_dict = specContent_dict.replace('-', ' ')
                self.save_desc(fk_prod, 3, "c_name", specContent_dict)
            elif '퓨전APU-A4-' in specContent_dict:
                specContent_dict = specContent_dict.replace('퓨전APU-A4-', 'AMD ')
                self.save_desc(fk_prod, 3, "c_name", specContent_dict)
            elif id_dict == 130715:
                self.save_desc(fk_prod, 3, "c_co", specContent_dict)
            elif id_dict == 130713:
                self.save_desc(fk_prod, 3, "c_gen", specContent_dict)
            elif id_dict == 211238:
                self.save_desc(fk_prod, 3, "c_unit", specContent_dict)
            elif id_dict == 211239:
                self.save_desc(fk_prod, 3, "c_low_speed", specContent_dict)
            elif id_dict == 130733:
                self.save_desc(fk_prod, 3, "c_top_speed", specContent_dict)
            else:
                self.save_desc(fk_prod, 3, None, specContent_dict)

        elif id_dict == 219055:
            self.save_desc(fk_prod, 3, "c_name", 'Snapdragon 7c')
        # ================================= 내장 그래픽 =========================================
        elif id_dict in gpu_option:
            if "Iris Xe" in specContent_dict:
                specContent_dict = specContent_dict.replace('Iris Xe', 'Intel Iris Xe')
            elif "UHD Graphics" in specContent_dict:
                specContent_dict = specContent_dict.replace('UHD Graphics', 'Intel UHD Graphics')
            elif "라데온 Graphics" in specContent_dict:
                specContent_dict = specContent_dict.replace('라데온 Graphics', 'Radeon Graphics')
            elif "라데온 660M" in specContent_dict:
                specContent_dict = specContent_dict.replace('라데온 660M', 'Radeon Graphics')
            elif "라데온 680M" in specContent_dict:
                specContent_dict = specContent_dict.replace('라데온 680M', 'Radeon Graphics')
            elif "라데온 RX Vega" in specContent_dict:
                if "Vega 3" in specContent_dict:
                    specContent_dict = specContent_dict.replace('라데온 RX Vega 3', 'Radeon Vega 3 Mobile')
                else:
                    specContent_dict = specContent_dict.replace('라데온 RX Vega', 'Radeon RX Vega')
            self.save_desc(fk_prod, 4, None, specContent_dict)

        # ================================= 외장 그래픽 =========================================
        elif specGroupname_id_dict in ext_gpu_option:
            if "RTX" in specContent_dict:
                specContent_dict = specContent_dict.replace('RTX', 'RTX ')
                if "RTX  A" in specContent_dict:
                    specContent_dict = specContent_dict.replace('RTX  A', 'RTX A')
            elif "GTX" in specContent_dict:
                specContent_dict = specContent_dict.replace('GTX', 'GTX ')
            elif "쿼드로" in specContent_dict:
                specContent_dict = specContent_dict.replace('쿼드로 ', 'Quadro ')
            elif "라데온RX" in specContent_dict:
                specContent_dict = specContent_dict.replace('라데온RX', 'Radeon RX ')
            self.save_desc(fk_prod, 5, "g_name", specContent_dict)
        elif id_dict in ext_gpu_option:
            if id_dict == 130628:
                self.save_desc(fk_prod, 5, "g_memory", specContent_dict)
            elif id_dict == 218699:
                self.save_desc(fk_prod, 5, "g_tgp", specContent_dict)
            else:
                self.save_desc(fk_prod, 5, None, specContent_dict)

        # ================================= RAM =========================================
        elif id_dict in ram_option:
            if id_dict == 210963:
                self.save_desc(fk_prod, 6, "ram_ddr", specContent_dict)
            elif id_dict == 130643:
                if "확인 후 구매" in specContent_dict:
                    self.save_desc(fk_prod, 6, "ram_cap", "직접확인")
                else:
                    self.save_desc(fk_prod, 6, "ram_cap", specContent_dict)

        # ================================= 저장장치 =========================================
        elif id_dict in stge_option:
            if id_dict == 130680: # SSD
                if "확인 후 구매" in specContent_dict:
                    self.save_desc(fk_prod, 7, "stg_cap_ssd", "직접확인")
                else:
                    self.save_desc(fk_prod, 7, "stg_cap_ssd", specContent_dict)
            elif id_dict == 130678: # HDD:
                if "확인 후 구매" in specContent_dict:
                    self.save_desc(fk_prod, 7, "stg_cap_hdd", "직접확인")
                else:
                    self.save_desc(fk_prod, 7, "stg_cap_hdd", specContent_dict)
            elif id_dict == 216825: # eMMC
                if "확인 후 구매" in specContent_dict:
                    self.save_desc(fk_prod, 7, "stg_cap_emmc", "직접확인")
                else:
                    self.save_desc(fk_prod, 7, "stg_cap_emmc", specContent_dict)
            else:
                self.save_desc(fk_prod, 7, None, specContent_dict)

        # ================================= 배터리 =========================================
        elif id_dict in battery_option:
            if id_dict == 213912:
                self.save_desc(fk_prod, 8, "battery_wh", specContent_dict)
            else:
                self.save_desc(fk_prod, 8, None, specContent_dict)

        # ================================= 무게, 두께 =========================================
        elif id_dict == 130644: # 무게
            self.save_desc(fk_prod, 9, 'wt', specContent_dict)
        elif id_dict == 130641: # 두께
            self.save_desc(fk_prod, 9, 'thk', specContent_dict)

        # ================================= 부가기능 =========================================
        elif id_dict == 130687:
            self.save_desc(fk_prod, 10, None, "웹캠 전면")
        elif id_dict in add_option:
            self.save_desc(fk_prod, 10, None, specContent_dict)
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
                time.sleep(0.25)
        # self.save_desc(Prod.objects.get(prod_id=87291419), 3, "c_name", "i7-11850H")
        # self.save_desc(Prod.objects.get(prod_id=87291711), 3, "c_name", "i7-11850H")
        # self.save_desc(Prod.objects.get(prod_id=86353204), 4, None, "Intel UHD Graphics")
        # self.save_desc(Prod.objects.get(prod_id=94001758), 3, 'c_name', "i7-1260P")
        # self.save_desc(Prod.objects.get(prod_id=97180767), 2, 'd_res', "1920x1200(WUXGA)")
        print("누락 DB 저장 완료")
    # ===================================================================================

if __name__ == '__main__':
    result = enuri()
    result.prodDesc()
    print("크롤링이 완료되었습니다.")