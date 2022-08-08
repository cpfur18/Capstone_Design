"""
교보문고 크롤링 코드
"""
# 셀레니움 import
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# BeautifulSoup import
from bs4 import BeautifulSoup
import time

class Kyobo_croller:
    # 크롬 드라이버 초기화
    def init_driver(self, url):
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
        driver.get(url)
        # driver.get('https://book.naver.com/bestsell/bestseller_list.naver')

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

    # 네이버 url 추출
    def book_page_url(self, driver):
        page_urls_book = []
        for i in range(0, 25):
            list_book = driver.select(f'#section_bestseller > ol > li:nth-child({i})')
            link_book = list_book.select.one('#section_bestseller > ol > li:nth-child(1) > div > div > a').get('href')

            page_urls_book.append(link_book)
        return page_urls_book

    def page_urls_kyobo(self, driver):
        kyobo_page_urls = []
        for index in range(0, 1):
            review_link_kyobo = driver.select_one('#productListLayer > ul > li:nth-child(2) > div > a.N\=a\:buy\.cplist\,r\:2\,i\:kyobo').get('href')
            kyobo_page_urls.append(review_link_kyobo)
        return kyobo_page_urls

    # 크롤링 함수
    def crolling(self, page_urls_book):

        for index, page_urls_book in enumerate(page_urls_book):

            driver = self.init_driver(page_urls_book)
            soup = self.init_bs4(driver)

            # title, isbn 추출
            title = soup.select_one('#container > div.spot > div.book_info > h2 > a').text
            isbn = soup.select_one('#container > div.spot > div.book_info > div.book_info_inner > div:nth-child(3)').text

            # index, title, isbn 출력
            print(index + 1, title, isbn)

            kyobo_page_urls = self.page_urls_kyobo(driver)
            print(kyobo_page_urls)

        # 문제인 부분
        for index, kyobo_page_url in enumerate(kyobo_page_urls):

            driver(kyobo_page_urls + '#review')
            soup = self.init_bs4(driver)

            = self.book_page_url
            a = driver.select('dd.comment > div.txt')

            for asd in a:
                kyobo_review = asd.text
                print(f'kyobo_review = {kyobo_review}')

    def start_crolling(self):
        # webdirver 설정
        driver = self.init_driver()

        self.Kyobo_croller(self.init_bs4(driver))

        self.select_button(2, driver)
        time.sleep(3)
        self.cpu_croll(self.init_bs4(driver))

        # 브라우저 종료
        driver.close()

result = cpu_mark()
result.cpu_benchmark()