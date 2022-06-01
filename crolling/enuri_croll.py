"""
에누리 크롤링 코드
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
from note_book_service.models import Prod, Prod_property


# 셀레니움 import
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# BeautifulSoup import
from bs4 import BeautifulSoup
import time
class enuri:
    # 크롬 드라이버 초기화
    def init_driver(self):
        options = Options()
        driver = webdriver.Chrome(options=options)

        # 브라우저 내부 대기
        driver.implicitly_wait(5)

        # chrom headless 모드 동작
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")

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
        new_prod = "#listBodyDiv > div.list-body > div.list-body-cont > div.list-filter > div.list-filter-bot > ul > li:nth-child(4)"
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, new_prod))).click()
        # review_count = "#listBodyDiv > div.list-body > div.list-body-cont > div.list-filter > div.list-filter-bot > ul > li:nth-child(6)"
        # WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, review_count))).click()

    # 크롤링 함수
    def enuri_crolling(self, driver, spage, lpage):
        # 마지막 페이지까지 반복
        while spage <= lpage:
            soup = self.init_bs4(driver)
            # 상품 리스트에 저장
            notebook_list = soup.select('li.prodItem')

            for item_list in notebook_list:
                # 상품명, 스펙, 가격 변수 저장
                model_id = item_list.attrs["data-model-origin"]
                company = item_list.select_one('li.item__etc--brand > a').text.strip()
                name = item_list.select_one('div.item__model > a').text.strip()
                price = item_list.select_one('div.opt--price > span').text.strip()
                # 2년 내 출시
                reg_date = item_list.select_one('li.item__etc--date').text.strip()
                review_count = item_list.select_one('li.item__etc--score').text.strip()
                spec = item_list.select_one('ul.item__attr').text.strip()
                print(model_id, company, name, price, reg_date, review_count)

                # 상품 정보 DB저장
                Prod(prod_id=model_id ,prod_company=company, prod_name=name, prod_price=price, prod_reg_date=reg_date, prod_review_count=review_count).save()

                # 상품 옵션 DB 저장
                spec_list = spec.split('|')
                fk_prod = Prod.objects.get(prod_id=model_id)

                for prod_list in spec_list:

                    Prod_property(prod_id=fk_prod, prod_property=prod_list).save()
                    # print(prod_list)

                #이미지 링크 변수 저장
                    # img_link = item_list.select_one('div.thumb_image > a > img').get('data-original')
                    # if img_link == None:
                    #     img_link = item_list.select_one('div.thumb_image > a > img').get('src')

                    # 상품 스펙 인덱싱 후 리스트 저장
                    # spec_number = spec.split(' / ')

                    # print(name, spec)

            # 페이지 변수 증가
            spage += 1

            # 페이지 넘기기
            nextPage = 'div.paging__inner > a:nth-child({})'.format(spage)
            # 페이지 버튼 클릭
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, nextPage))).click()

            # BeautifulSoup 값 삭제
            del soup

            # 3초간 대기
            time.sleep(3)

    def enuri_croll(self):
        driver = self.init_driver()

        self.button_click(driver)
        time.sleep(2)

        self.enuri_crolling(driver, 1, 6)

        # 브라우저 종료
        driver.close()

result = enuri()
result.enuri_croll()