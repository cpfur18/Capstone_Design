"""
에누리 크롤링 코드
"""
# 멀티 프로세싱
from multiprocessing import Pool

# Django import
import os
import sys

# 프로젝트 절대경로
sys.path.append('D:\Capstone_Design\config')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# 웹프레임워크
import django

django.setup()
from note_book_service.models import Prod, Prod_property, Prod_img
import urllib.request

# 셀레니움 import
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# BeautifulSoup import
from bs4 import BeautifulSoup
import time

class enuri:
    # 크롬 드라이버 초기화
    def init_driver(self):
        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome()

        # 브라우저 내부 대기
        driver.implicitly_wait(5)

        # url 접근
        driver.get('http://www.enuri.com/list.jsp?cate=0404')

        return driver

    # bs4 초기화
    def init_bs4(self, driver):
        # 페이지 소스 가져오기
        source = driver.page_source
        # bs4 초기화
        soup = BeautifulSoup(source, 'html.parser')
        return soup

    # 버튼 클릭
    def button_click(self, driver):
        comparison_price = "#listBodyDiv > div.list-body > div.list-body-cont > div.list-filter > div.list-filter-top > ul > li:nth-child(2) > a"
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, comparison_price))).click()
        time.sleep(1)
        new_prod = "#listBodyDiv > div.list-body > div.list-body-cont > div.list-filter > div.list-filter-bot > ul > li:nth-child(4)"
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, new_prod))).click()
        time.sleep(1)

# 이미지 크롤링
class enuri_img(enuri):
    def enuri_crolling_img(self, driver, spage, lpage):
        lpage /= 10
        last = 0
        count = 0
        # 마지막 페이지까지 반복
        while last != lpage:
            soup = self.init_bs4(driver)
            time.sleep(1)
            # 상품 리스트에 저장
            notebook_list = soup.select('li.prodItem')
            time.sleep(1)
            for item_list in notebook_list:
                # 상품명, 가격 저장
                model_id = item_list.attrs["data-model-origin"]
                images = item_list.select_one("div.item__thumb > a > img").get('src')
                try:
                    Prod_img.objects.get(prod_id=model_id)
                    print("PASS")
                except:
                    # img_url.append(images)
                    print(model_id, " : ", images)
                    urllib.request.urlretrieve(images, f'D:/Capstone_Design/static/assets/img/{model_id}.jpg')
                    try:
                        fk_prod = Prod.objects.get(prod_id=model_id)
                        Prod_img(prod_id=fk_prod, prod_img_src=f'static/assets/img/{model_id}').save()
                        count += 1
                    except:
                        print("Img Crolling errer(Prod_id not found)")
                        continue
            print('===============================================')
            print('반복횟수 : ', count)
            # 페이지 변수 증가
            spage += 1

            # 페이지 넘기기
            nextPage = 'div.paging__inner > a:nth-child({})'.format(spage)
            nextbutton = '#listBodyDiv > div.list-body > div.list-body-cont > div.goods-list > div.paging > div > button.paging__btn--next > i'
            if spage == 11:
                # 페이지 버튼 클릭
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, nextbutton))).click()
                spage = 1
                last += 1
            else:
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, nextPage))).click()

            # BeautifulSoup 값 삭제
            del soup

            # 10초간 대기
            time.sleep(5)

    def enuri_img_croll(self):
        driver = self.init_driver()

        self.button_click(driver)
        time.sleep(2)

        self.enuri_crolling_img(driver, 1, 300)

        # 브라우저 종료
        print("크롤링이 끝났습니다.")
        driver.close()


if __name__=='__main__':
    start_time = time.time()

    # 이미지 크롤링
    result = enuri_img()
    result.enuri_img_croll()