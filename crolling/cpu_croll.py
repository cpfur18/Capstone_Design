"""
CPU 크롤링 코드
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
from note_book_service.models import Passmark_cpu_info

# cpu_name = models.CharField(max_length=30, verbose_name='cpu_이름')
# cpu_mark = models.IntegerField(verbose_name='cpu_벤치마크')

# 셀레니움 import
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# BeautifulSoup import
from bs4 import BeautifulSoup
import time

class cpu_mark:
    # 크롬 드라이버 초기화
    def init_driver(self):
        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome()

        # 브라우저 내부 대기
        driver.implicitly_wait(5)

        # url 접근
        driver.get('https://www.cpubenchmark.net/CPU_mega_page.html')

        return driver

    # 카테고리 드롭박스 클릭
    def select_button(self, option, driver):
        category = "#search_category > option:nth-child({})".format(option)
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, category))).click()

    # 정렬 클릭
    def sort_button(self, driver):
        sorting = "#cputable > thead > tr > th:nth-child(4)"
        sort = "#cputable_length > label > select > option:nth-child(4)"
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, sorting))).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, sort))).click()

    # bs4 초기화
    def init_bs4(self, driver):
        # 페이지 소스 가져오기
        source = driver.page_source
        # bs4 초기화
        soup = BeautifulSoup(source, 'html.parser')
        return soup

    # 크롤링 함수
    def cpu_croll(self, soup):
            # CPU 리스트 저장
            cpu_list = soup.select('table.dataTable-blue.dataTable.no-footer > tbody > tr')

            for cputable in cpu_list:
            # CPU_이름, CPU_벤치마크_정보 저장
                name = cputable.select_one('td > a').text
                mark = cputable.select_one('td.sorting_1').text
                # 숫자 단위 콤마 제거

                name = name.split(" @ ")[0]
                mark = int(mark.replace(",", ""))

                print(name, mark)

                # DB 저장
                if "AMD Ryzen 7 4800HS" in name:
                    print("AMD Ryzen 7 4800HS")
                    continue
                if "Intel Core i7-1185G7E" in name:
                    print("Intel Core i7-1185G7E")
                    continue
                if "Intel Core i5-8365UE" in name:
                    print("Intel Core i5-8365UE")
                    continue
                if "Intel Pentium 5405U" in name:
                    print("Intel Pentium 5405U")
                    Passmark_cpu_info(cpu_name="Intel Pentium G5405U", cpu_mark=2269).save()
                if "Intel Celeron N4020C" in name:
                    continue
                else:
                    if "Intel Xeon W-" in name:
                        name = name.replace('Intel Xeon W-', '제온W-')
                    Passmark_cpu_info(cpu_name=name, cpu_mark=mark).save()

    def cpu_benchmark(self):
        # webdirver 설정
        driver = self.init_driver()

        # 1차 크롤링
        self.select_button(4, driver)
        self.sort_button(driver)
        time.sleep(3)
        self.cpu_croll(self.init_bs4(driver))

        # 2차 크롤링
        self.select_button(2, driver)
        time.sleep(3)
        self.cpu_croll(self.init_bs4(driver))

        # 누락된 CPU 벤치마크 정보 
        Passmark_cpu_info(cpu_name="AMD Ryzen 5 4650U", cpu_mark=12836).save()
        Passmark_cpu_info(cpu_name="AMD Ryzen 5 4680U", cpu_mark=12900).save()
        Passmark_cpu_info(cpu_name="AMD Ryzen 7 4980U", cpu_mark=17017).save()
        Passmark_cpu_info(cpu_name="Intel Pentium G6405U", cpu_mark=2370).save()
        Passmark_cpu_info(cpu_name="Intel Celeron N4020", cpu_mark=1570).save()
        Passmark_cpu_info(cpu_name="Intel Celeron N4500", cpu_mark=1914).save()
        Passmark_cpu_info(cpu_name="AMD Ryzen 5 6600HS", cpu_mark=20400).save()

        # 브라우저 종료
        driver.close()

result = cpu_mark()
result.cpu_benchmark()
