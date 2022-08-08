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

if select >= 1 or select == 4:

    # 에누리 노트북 정보 크롤링
    if select == 1:
        # 페이지 시작 끝 설정
        startPage = 1
        lastPage = 6


    # 노트북 리뷰 크롤링
    if select == 2:
        # 페이지 시작 끝 설정
        startPage = 1
        lastPage = 6
        # 에누리 노트북 정보 크롤링 함수 실행
        # enuri_croll.croll(startPage, lastPage)

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