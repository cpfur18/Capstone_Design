"""
에누리 크롤링 코드
"""
#멀티 프로세싱
from multiprocessing import Pool

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
import urllib.request


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
        time.sleep(1)
        new_prod = "#listBodyDiv > div.list-body > div.list-body-cont > div.list-filter > div.list-filter-bot > ul > li:nth-child(4)"
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, new_prod))).click()
        time.sleep(1)

    # 크롤링 함수
    def enuri_crolling(self, driver, spage, lpage):

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
                # 상품명, 제조사 가격, 상품 등록일 저장
                model_id = item_list.attrs["data-model-origin"]
                company = item_list.select_one('li.item__etc--brand > a').text.strip()
                name = item_list.select_one('div.item__model > a').text.strip()
                price = item_list.select_one('div.opt--price > span').text.strip()
                reg_date = item_list.select_one('li.item__etc--date').text.strip()
                # 리뷰 평점 및 개수 인덱싱 후 저장
                review_count = item_list.select_one('li.item__etc--score').text.split()
                count += 1

                # 상세 옵션
                spec = item_list.select_one('ul.item__attr').text.strip()
                if not review_count:
                    print(model_id, company, name, price, reg_date)
                else:
                    print(model_id, company, name, price, reg_date, review_count[0], review_count[1])
                # 기본 정보 DB저장
                if not review_count:
                    Prod(prod_id=model_id, prod_company=company, prod_name=name, prod_price=price, prod_reg_date=reg_date).save()
                else:
                    Prod(prod_id=model_id, prod_company=company, prod_name=name, prod_price=price, prod_reg_date=reg_date, prod_review_grade=review_count[0], prod_review_count=review_count[1].strip('('')')).save()
                # 상품 옵션 DB 저장
                spec_list = spec.split('|')
                fk_prod = Prod.objects.get(prod_id=model_id)

                for prod_list in spec_list:
                    Prod_property(prod_id=fk_prod, prod_property=prod_list).save()
                    # print(prod_list)
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

            # 3초간 대기
            time.sleep(3)

    def enuri_croll(self):
        driver = self.init_driver()

        self.button_click(driver)
        time.sleep(4)

        self.enuri_crolling(driver, 1, 30)

        # 브라우저 종료
        print("크롤링이 끝났습니다.")
        driver.close()

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
                # img_url.append(images)
                print(model_id, " : ", images)
                urllib.request.urlretrieve(images, f'D:/Capstone_Design/static/assets/img/{model_id}.jpg')

                fk_prod = Prod.objects.get(prod_id=model_id)
                Prod_img(prod_id=fk_prod, prod_img_src=f'static/assets/img/{model_id}').save()
                count += 1

 
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
            time.sleep(3)

    def enuri_img_croll(self):
        driver = self.init_driver()

        self.button_click(driver)
        time.sleep(2)

        self.enuri_crolling_img(driver, 1, 30)

        # 브라우저 종료
        print("크롤링이 끝났습니다.")
        driver.close()

if __name__=='__main__':
    start_time = time.time()
    # result = enuri()
    # result.enuri_croll()

    # 이미지 크롤링
    result = enuri_img()
    result.enuri_img_croll()

    #멀티 프로세싱
    # pool = Pool(processes=4)
    # pool.map(result.enuri_croll())
    # pool.close()
    # pool.join()