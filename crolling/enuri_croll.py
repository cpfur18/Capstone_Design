"""
에누리 크롤링 코드
"""

#Django import
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# 웹프레임워크
import django
django.setup()

# 셀레니움 import
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# BeautifulSoup import
from bs4 import BeautifulSoup
import time

# 크롬 드라이버 초기화
def init_driver():
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
def init_bs4(driver):
    # 페이지 소스 가져오기
    source = driver.page_source
    # bs4 초기화
    soup = BeautifulSoup(source, 'html.parser')
    return soup

# 버튼 클릭
def button_click():
    comparison_price = "#listBodyDiv > div.list-body > div.list-body-cont > div.list-filter > div.list-filter-top > ul > li:nth-child(2) > a"
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, comparison_price))).click()
    review_count = "#listBodyDiv > div.list-body > div.list-body-cont > div.list-filter > div.list-filter-bot > ul > li:nth-child(6)"
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, review_count))).click()

# 크롤링 함수
def enuri_croll(soup):
    # 마지막 페이지까지 반복
    # while spage <= lpage:

    # 상품 리스트에 저장
    notebook_list = soup.select('li.prodItem')

    # 더미 데이터 삭제
    #del notebook_list[30]

    # class Prod(models.Model):
    #     prod_num = models.AutoField(primary_key=True, verbose_name='노트북_번호')
    #     prod_company = models.CharField(max_length=30, verbose_name='노트북_제조사')
    #     prod_name = models.CharField(max_length=100, verbose_name='노트북_이름')
    #     prod_price = models.CharField(max_length=100, verbose_name='노트북_가격')
    #     prod_reg_date = models.CharField(max_length=100, verbose_name='노트북_등록일')
    #     prod_review_count = models.IntegerField(verbose_name='노트북_리뷰수')

    for item_list in notebook_list:
        # 상품명, 스펙, 가격 변수 저장
        company = item_list.select_one('li.item__etc--brand > a').text.strip()
        name = item_list.select_one('div.item__model > a').text.strip()
        price = item_list.select_one('div.opt--price > span').text.strip()
        # 2년 내 출시
        reg_date = item_list.select_one('li.item__etc--date').text.strip()
        #90개씩 리뷰 개수 50개 이상
        review_count = item_list.select_one('li.item__etc--score').text.strip()
        spec = item_list.select_one('ul.item__attr').text.strip()
        print(company, name, price, reg_date, review_count)

            #이미지 링크 변수 저장
            # img_link = item_list.select_one('div.thumb_image > a > img').get('data-original')
            # if img_link == None:
            #     img_link = item_list.select_one('div.thumb_image > a > img').get('src')

            # 상품 스펙 인덱싱 후 리스트 저장
            # spec_number = spec.split(' / ')

            # print(name, spec)

        # 페이지 변수 증가
        # spage += 1

        # 페이지 넘기기
        # nextPage = 'div.number_wrap > a:nth-child({})'.format(spage)
        # 페이지 버튼 클릭
        # WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, nextPage))).click()

        # BeautifulSoup 값 삭제
        # del soup

        # 3초간 대기
        # time.sleep(3)

# webdirver 설정
driver= init_driver()

# 버튼 클릭
button_click()

# 렌더링 대기
time.sleep(2)

soup = init_bs4(driver)

enuri_croll(soup)

# 브라우저 종료
driver.close()