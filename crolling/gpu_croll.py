"""
GPU 크롤링 코드
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
from note_book_service.models import Passmark_gpu_info

# 셀레니움 import
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# BeautifulSoup import
from bs4 import BeautifulSoup
import time
class gpu_mark:
    # 크롬 드라이버 초기화
    def init_driver(self):
        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome()

        # 브라우저 내부 대기
        driver.implicitly_wait(5)

        # url 접근
        driver.get('https://www.videocardbenchmark.net/GPU_mega_page.html')

        return driver

    # 카테고리 드롭박스 클릭
    def select_button(self, option, driver):
        category = "#search_category > option:nth-child({})".format(option)
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, category))).click()
        # search_category > option:nth-child(2, 4)
    # 정렬 클릭
    def sort_button(self, driver):
        sorting = "#cputable > thead > tr > th:nth-child(3)"
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
    def gpu_croll(self, soup):
            # GPU 리스트 저장
            gpu_list = soup.select('table.dataTable-blue.dataTable.no-footer > tbody > tr')

            for gputable in gpu_list:
            # GPU_이름, GPU_벤치마크_정보 저장
                name = gputable.select_one('td > a').text
                mark = gputable.select_one('td.sorting_1').text

                # 숫자 단위 콤마 제거
                mark = int(mark.replace(",", ""))
                print(name, mark)

                # DB 저장
                Passmark_gpu_info(gpu_name=name, gpu_mark=mark).save()

    def gpu_benchmark(self):
        # webdirver 설정
        driver = self.init_driver()

        # 1차 크롤링
        self.select_button(4, driver)
        self.sort_button(driver)
        time.sleep(2)
        self.gpu_croll(self.init_bs4(driver))

        # 2차 크롤링
        self.select_button(2, driver)
        time.sleep(2)
        self.gpu_croll(self.init_bs4(driver))

        # 브라우저 종료
        driver.close()

result = gpu_mark()
result.gpu_benchmark()