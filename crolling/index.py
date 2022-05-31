from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import enuri_croll
# import prod_review_croll
import cpu_croll
import gpu_croll

"""
파이썬 크롤링 스크립트 실행
"""
print('============================================\n')
print("크롤링을 진행할 작업을 숫자를 입력해 선택 하세요.   \n")
print("1 : 노트북 정보       2 : 노트북 리뷰\n3 : CPU 벤치마크       4 : GPU 벤치마크")
print('============================================\n')
select = input("실행할 명령을 입력하세요 :")

if select >= 1 & select == 4:

    # 에누리 노트북 정보 크롤링
    if select == 1:
        # 페이지 시작 끝 설정
        startPage = 1
        lastPage = 6

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
        enuri_croll.croll(startPage, lastPage)


    # 노트북 리뷰 크롤링
    if select == 2:
        # 페이지 시작 끝 설정
        startPage = 1
        lastPage = 6
        # 에누리 노트북 정보 크롤링 함수 실행
        enuri_croll.croll(startPage, lastPage)

    # CPU 벤치마크 크롤링
    if select == 3:
        cpu_croll.cpu_benchmark()
        print("벤치마크 크롤링이 완료 되었습니다.")

    # GPU 벤치마크 크롤링
    if select == 4:
        gpu_croll.gpu_benchmark()
        print("벤치마크 크롤링이 완료 되었습니다.")

else:
    print ("잘못된 입력 입니다.")

# GPU 벤치마크 크롤링 함수 실행