"""
옵션 수치화 코드
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

class Get_score_Prod:
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

            if 0 <= mark <= 10:
                score_cpu = 1
            elif 11 <= mark <= 20:
                score_cpu = 1.5
            elif 21 <= mark <= 30:
                score_cpu = 2
            elif 31 <= mark <= 40:
                score_cpu = 2.5
            elif 41 <= mark <= 50:
                score_cpu = 3
            elif 51 <= mark <= 60:
                score_cpu = 3.5
            elif 61 <= mark <= 70:
                score_cpu = 4
            elif 71 <= mark <= 80:
                score_cpu = 4.5
            else:
                score_cpu = 5
        except:
            print("CPU : Error")

        return score_cpu

    def gpu_score(self, spec_prod, mark_gpu_prod, bool_gpu):
        try:
            if bool_gpu:
                getNameGpu = spec_prod.filter(option_title__icontains='g_name').values('option_Content')
                NameGpu = list(getNameGpu.get(option_Content__contains=getNameGpu).values())[0]
                print("GPU NAME :", NameGpu)
            else:
                getNameGpu = spec_prod.filter(option_id=4).values('option_Content')
                getNameCpu = spec_prod.filter(option_title__icontains='c_name').values('option_Content')
                NameCpu = list(getNameCpu.get(option_Content__contains=getNameCpu).values())[0]
                NameGpu = list(getNameGpu.get(option_Content__contains=getNameGpu).values())[0]

                if "Ryzen " in NameCpu:
                    if "Vega" not in NameGpu:
                        amd__ =["5625U", "5825U", "5425U", "4680U"]
                        if any(keyword in NameCpu for keyword in amd__):
                            print("GPU NAME :", NameGpu)
                        else:
                            getNameGpu = NameCpu + " with " + NameGpu
                            print(getNameGpu)
                else:
                    print("GPU NAME :" + NameGpu)

            cent_gpu = 22199 / 100
            if not bool_gpu:

                if "Ryzen 7 PRO 6850HS" in NameCpu:
                    getNameGpu = NameCpu + " with Radeon Graphics"
                    getMarkGpu = mark_gpu_prod.filter(gpu_name__exact=getNameGpu).values('gpu_mark').first()
                    getMarkGpu = list(getMarkGpu.values())

                elif "Ryzen 7 PRO 6850H" in NameCpu:
                    getNameGpu = NameCpu + " with Radeon Graphics"
                    getMarkGpu = mark_gpu_prod.filter(gpu_name__exact=getNameGpu).values('gpu_mark').first()
                    getMarkGpu = list(getMarkGpu.values())

                elif "Ryzen 5 PRO 5675U" in NameCpu:
                    getNameGpu = NameCpu + " with Radeon Graphics"
                    getMarkGpu = mark_gpu_prod.filter(gpu_name__exact=getNameGpu).values('gpu_mark').first()
                    getMarkGpu = list(getMarkGpu.values())

                elif "Ryzen 5 PRO 5675" in NameCpu:
                    getNameGpu = NameCpu + " with Radeon Graphics"
                    getMarkGpu = mark_gpu_prod.filter(gpu_name__exact=getNameGpu).values('gpu_mark').first()
                    getMarkGpu = list(getMarkGpu.values())

                else:
                    getMarkGpu = mark_gpu_prod.filter(gpu_name__icontains=getNameGpu).values('gpu_mark').first()
                    getMarkGpu = list(getMarkGpu.values())

            else:
                getMarkGpu = mark_gpu_prod.filter(gpu_name__icontains=getNameGpu).values('gpu_mark').first()
                getMarkGpu = list(getMarkGpu.values())

            mark = int(round(getMarkGpu[0] / cent_gpu, 0))

            if 0 <= mark <= 10:
                score_gpu = 1
            elif 11 <= mark <= 20:
                score_gpu = 1.5
            elif 21 <= mark <= 30:
                score_gpu = 2
            elif 31 <= mark <= 40:
                score_gpu = 2.5
            elif 41 <= mark <= 50:
                score_gpu = 3
            elif 51 <= mark <= 60:
                score_gpu = 3.5
            elif 61 <= mark <= 70:
                score_gpu = 4
            elif 71 <= mark <= 80:
                score_gpu = 4.5
            else:
                score_gpu = 5

        except:
            print("GPU : Error")

        return score_gpu

    def ram_score(self, spec_prod):
        """
        4GB 1점, 8GB 2점 16gb 3점 32GB↑ 4점, DDR4,5 +1점 LP면 추가 안함
        """
        ram = spec_prod.filter(option_id=6).values('option_title', 'option_Content')
        cap_ram = ram.get(option_title='ram_cap') # ram_cap(용량)
        cap_ram = list(cap_ram.values())
        replace_ram = int(cap_ram[1].replace('GB', ''))

        print("RAM :", cap_ram[1])

        if replace_ram <= 4:
            score_ram = 1
        elif 4 < replace_ram <= 8:
            score_ram = 2
        elif 8 < replace_ram <= 12:
            score_ram = 3
        elif 12 < replace_ram <= 16:
            score_ram = 3.5
        elif 16 < replace_ram <= 32:
            score_ram = 4
        elif 32 < replace_ram <= 64:
            score_ram = 4.5
        elif replace_ram > 64:
            score_ram = 5

        return score_ram

    def stg_score(self, spec_prod):
        """
            128GB 아래 1 점  128GB 1.5점 256 2점 512 2.5점 1TB 3점 1.5 TB 3.5 2TB 4점
        """
        stg = spec_prod.filter(option_id=7).values('option_title', 'option_Content')
        ssd_check_stg = stg.filter(option_title='stg_cap_ssd').exists()
        hdd_check_stg = stg.filter(option_title='stg_cap_hdd').exists()
        emmc_check_stg = stg.filter(option_title='stg_cap_emmc').exists()
        score_stg = 0

        print("SSD :", ssd_check_stg, "|", "HDD :", hdd_check_stg, "|", "eMMc :", emmc_check_stg)

        if ssd_check_stg | hdd_check_stg | emmc_check_stg:
            if ssd_check_stg:
                cap_stg_ssd = stg.filter(option_title='stg_cap_ssd').values('option_Content')  # stg_cap(용량)
                ssd_stg = list(cap_stg_ssd.get(option_Content__contains=cap_stg_ssd).values())[0]

                if "직접확인" in ssd_stg:
                    score_stg = None

                else:
                    cap_stg = int(re.sub(r'[^0-9]', '', ssd_stg))
                    if 32 <= cap_stg <= 128:
                        score_stg = 1
                    elif 128 <= cap_stg < 256:
                        score_stg = 2
                    elif 256 <= cap_stg < 512:
                        score_stg = 3
                    elif 512 <= cap_stg:
                        score_stg = 4
                    elif 1 <= cap_stg <= 16:
                        score_stg = 4.5

            if hdd_check_stg:
                cap_stg_hdd = stg.filter(option_title='stg_cap_hdd').values('option_Content')
                hdd_stg = list(cap_stg_hdd.get(option_Content__contains=cap_stg_hdd).values())[0]
                if "직접확인" not in hdd_stg:
                    score_stg += 0.5

            if emmc_check_stg:
                cap_stg_emmc = stg.filter(option_title='stg_cap_emmc').values('option_Content')
                emmc_stg = list(cap_stg_emmc.get(option_Content__contains=cap_stg_emmc).values())[0]
                if "직접확인" not in emmc_stg:
                    score_stg += 0.5
        else:
            print("stg : 미확인")
            score_stg = 0

        return score_stg
    # ==============================================================

    # ========================== 화면 ===============================
    def CheckSize(self, disp):
        if disp < 13:
            score_size_disp = 1
        elif 13 <= disp < 14:
            score_size_disp = 2
        elif 14 <= disp < 15.6:
            score_size_disp = 2.5
        elif disp == 15.6:
            score_size_disp = 3
        elif 15.6 <= disp < 17:
            score_size_disp = 4
        elif 17 <= disp:
            score_size_disp = 5
        return score_size_disp

    def size_display_score(self, spec_prod):
        """
        code 2 : 화면 크기
        """
        size_display = spec_prod.filter(Q(option_id=2) & Q(option_title='d_size')).values('option_Content')
        size_display = list(size_display.get(option_title__exact='d_size').values())[0]
        size_display = float(size_display.strip("인치"))

        score_size_disp = self.CheckSize(size_display)

        print("화면 크기 :", size_display, "인치")

        return score_size_disp

    def CheckResDisp(self, res_disp):
        res_low = ["1366", "1536"]
        if res_disp in res_low:
            score_res = 0.5
        elif "1600" in res_disp:
            score_res = 1
        else:
            score_res = 1.5
        return score_res

    def CheckPnlDisp(self, pnl_disp):
        pnl = ["OLED", "IPS"]
        if pnl_disp in pnl:
            score_pnl = 1
        else:
            score_pnl = 0.5
        return score_pnl

    def CheckColorDisp(self, disp):
        high_list = ["DCI-P3 120%", "DCI-P3 100%", "DCI-P3 99%", "NTSC 96%", "NTSC 94%", "NTSC 72%", "sRGB 135%",
                     "sRGB 130%", "sRGB 100%", "sRGB 96%"]
        middle_list = ["sRGB 62.5%", "NTSC 45%"]
        color_Disp_Score = 0
        try:
            color_disp = list(disp.get(option_title__contains='d_color').values())[0]
        except:
            dci = disp.filter(option_title__exact='d_color_dci').exists()
            srgb = disp.filter(option_title__exact='d_color_srgb').exists()
            argb = disp.filter(option_title__exact='d_color_argb').exists()

            if dci:
                color_disp = list(disp.get(option_title__exact='d_color_dci').values())[0]
            elif argb:
                color_disp = list(disp.get(option_title__exact='d_color_argb').values())[0]
            elif srgb:
                color_disp = list(disp.get(option_title__exact='d_color_srgb').values())[0]
            else:
                color_disp = list(disp.get(option_title__exact='d_color_ntsc').values())[0]

        if any(keyword in color_disp for keyword in high_list):
            color_Disp_Score += 1.5
        elif any(keyword in color_disp for keyword in middle_list):
            color_Disp_Score += 1
        else:
            color_Disp_Score += 0.5

        print("색재현률 : " + color_disp)

        return color_Disp_Score

    def CheckBhpDisp(self, bhp):
        bhp_score = 0
        bhp = int(bhp.replace('nit', ''))
        if bhp >= 300:
            bhp_score += 1
        if 250 <= bhp < 300:
            bhp_score += 0.5
        return bhp_score

    def display_score(self, spec_prod):
        """
        code 2 : 디스플레이
        1368 1600 1920
        """

        disp = spec_prod.filter(option_id=2).values('option_Content')
        score_disp = 0

        res_disp = list(disp.get(option_title__exact='d_res').values())[0]
        print("해상도 : " + res_disp)
        score_disp += self.CheckResDisp(res_disp)

        if disp.filter(option_title__exact='d_pnl').exists():
            pnl_disp = list(disp.get(option_title__exact='d_pnl').values())[0]
            print("패널 : " + pnl_disp)
            score_disp += self.CheckPnlDisp(pnl_disp)

        if disp.filter(option_title__contains='d_color').exists():
            score_disp += self.CheckColorDisp(disp)

        if disp.filter(option_title__exact='d_bhp').exists():
            bhp_disp = list(disp.get(option_title__exact='d_bhp').values())[0]
            print("밝기 : " + bhp_disp)
            score_disp += self.CheckBhpDisp(bhp_disp)

        return score_disp
    # ==============================================================

    # ========================== 휴대성 ==============================
    def CheckWeight(self, wt):
        wt = float(wt.replace('kg', ''))
        if wt <= 1:
            score = 3.5
        elif 1 < wt <= 1.5:
            score = 3
        elif 1.5 < wt <= 1.8:
            score = 2
        elif 1.8 < wt <= 2.3:
            score = 1.5
        elif 2.3 < wt <= 2.7:
            score = 1
        else:
            score = 0.5
        return score

    def getCarryScore(self, spec_prod):

        score_carry = 0
        spec_carry_prod = spec_prod.filter(option_id=9).values('option_Content')

        wt = list(spec_carry_prod.get(option_title__exact='wt').values())[0]
        print("무게 : " + wt)
        score_carry += self.CheckWeight(wt)

        if spec_prod.filter(Q(option_id=8) & Q(option_title__exact='battery_wh')).exists():
            battery_wh = spec_prod.filter(option_id=8).values('option_Content')
            battery_wh = list(battery_wh.get(option_title__exact='battery_wh').values())[0]
            print("배터리 용량 : " + battery_wh)
            battery_wh = float(battery_wh.replace('Wh', ''))

            if battery_wh >= 60:
                score_carry += 1.25
            elif 50 <= battery_wh < 60:
                score_carry += 1
            else:
                score_carry += 0.75

        if spec_prod.filter(Q(option_id=10) & Q(option_Content__exact='USB-PD')).exists():
            print("충전 단자 : " + "USB-PD")
            score_carry += 0.25
        else:
            print("충전 단자 : " + "DC")

        return score_carry
    # ==============================================================

    # ========================== 가격대 ==============================
    def CheckPrice(self, price_prod):
        if price_prod <= 600000:
            score = 5
        elif 600000 < price_prod <= 1000000:
            score = 4
        elif 1000000 < price_prod <= 1500000:
            score = 3.5
        elif 1500000 < price_prod <= 2000000:
            score = 3
        elif 2000000 < price_prod <= 2500000:
            score = 2.5
        elif 2500000 < price_prod <= 3000000:
            score = 2
        elif 3000000 < price_prod <= 3500000:
            score = 1.5
        else:
            score = 1

        return score

    def getPriceScore(self, id):
        price_prod = Prod.objects.filter(prod_id=id).values('prod_price')
        price_prod = list(price_prod.get(prod_id=id).values())[0]

        score = self.CheckPrice(price_prod)

        print("가격 : ", price_prod, score)

        return score
    # ==============================================================

class StartScore(Get_score_Prod):
    def saveDescScore(self, fk_prod, cpu, gpu, ram, stg, disp, disp_size, carry, price):
        Prod_ratings(prod_id=fk_prod, cpu=cpu, gpu=gpu, ram=ram, stg=stg, disp=disp, disp_size=disp_size,
                      carry=carry, price=price).save()

    def start(self):
        apple_list = [91571168, 91571201, 91571223, 91571229, 91571234, 91571238, 91571244, 91571252, 91571276,
                      91571299, 91571316, 91571328, 96329901, 96330001, 98764197]

        list_id_prod = Prod.objects.values('prod_id')
        list_spec_prod = Prod_property.objects.all()
        mark_cpu_prod = Passmark_cpu_info.objects.all()
        mark_gpu_prod = Passmark_gpu_info.objects.all()
        list_ratings_prod = Prod_ratings.objects.all()

        for id_prod in list_id_prod:
            id = int(id_prod.get('prod_id'))

            spec_prod = list_spec_prod.filter(prod_id__exact=id)
            check_gpu = spec_prod.filter(option_id=5).exists()
            print("=======================", id, "===========================")
            print(Prod.objects.get(prod_id=id), "\n")
            try:
                list_ratings_prod.get(prod_id=id)
                print("Check_prod : TRUE")
            except:
                if id not in apple_list:
                    cpu_score =self.getCpuScore(spec_prod, mark_cpu_prod)
                    print()
                    gpu_score = self.gpu_score(spec_prod, mark_gpu_prod, check_gpu)
                    print()
                    ram_score = self.ram_score(spec_prod)
                    print()
                    stg_score = self.stg_score(spec_prod)
                    print()
                    disp_size_score = self.size_display_score(spec_prod)
                    print()
                    disp_score = self.display_score(spec_prod)
                    print()
                    carry_score = self.getCarryScore(spec_prod)
                    print()
                    price_score = self.getPriceScore(id)
                    print()

                    print("CPU : ", cpu_score)
                    print("GPU : ", gpu_score)
                    print("RAM : ", ram_score)
                    print("STG : ", stg_score)
                    print("DISP_SIZE : ", disp_size_score)
                    print("DISP : ", disp_score)
                    print("휴대성 : ", carry_score)
                    print("가격 : ", price_score)

                    self.saveDescScore(Prod.objects.get(prod_id=id), cpu_score, gpu_score, ram_score, stg_score,
                                       disp_score, disp_size_score, carry_score, price_score)

            print("=========================================================\n")

if __name__ == '__main__':
    result = StartScore()
    result.start()
    print("작업 완료")
