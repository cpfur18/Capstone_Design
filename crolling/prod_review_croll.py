"""
에누리 크롤링 코드
"""

#Django import
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# 웹프레임워크
import django
django.setup()

from note_book_service.models import Prod
from note_book_service.models import Prod_property

# 셀레니움 import
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# BeautifulSoup import
from bs4 import BeautifulSoup
import time

# 크롤링 함수
def croll(spage, lpage):
    # 마지막 페이지까지 반복
    while spage <= lpage:

        # 페이지 소스 가져오기
        source = driver.page_source

        # bs4 초기화
        soup = BeautifulSoup(source, 'html.parser')

        # 상품 리스트에 저장
        notebook_list = soup.select('li.prod_item.prod_layer')

        # 더미 데이터 삭제
        #del notebook_list[30]

        for item_list in notebook_list:
            # 상품명, 스펙, 가격 변수 저장
            name = item_list.select_one('p.prod_name > a').text.strip()
            spec = item_list.select_one('dl.prod_spec_set > dd > div').text.strip()
            price = item_list.select_one('p.price_sect > a').text.strip()

            #이미지 링크 변수 저장
            # img_link = item_list.select_one('div.thumb_image > a > img').get('data-original')
            # if img_link == None:
            #     img_link = item_list.select_one('div.thumb_image > a > img').get('src')

            # 상품이름 인덱싱 후 리스트 저장
            name_slicing = name.split(' ')
            number = len(name_slicing[0])

            # 상품 스펙 인덱싱 후 리스트 저장
            spec_number = spec.split(' / ')

            # DB에 저장
            Prod(prod_company = name_slicing[0], prod_name = name[number + 1:], prod_price = price).save()

            n = Prod.objects.get(prod_name = name[number + 1:])
            for prod_list in spec_number:
                Prod_property(p_name = n, prod_property = prod_list).save()

            # print(name, spec)

        # 페이지 변수 증가
        spage += 1

        # 페이지 넘기기
        nextPage = 'div.number_wrap > a:nth-child({})'.format(spage)
        # 페이지 버튼 클릭
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, nextPage))).click()

        # BeautifulSoup 값 삭제
        del soup

        # 3초간 대기
        time.sleep(3)

# webdirver 설정
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

# 렌더링 대기
time.sleep(2)

# 브라우저 종료
driver.close()