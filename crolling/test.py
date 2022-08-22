"""
리뷰 크롤링 코드
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

# Json 크롤링
import json
import urllib.request as req

class review:
    # ============================ 상품 옵션 DB저장=============================================
    def prod_review(self):
        url = "http://www.enuri.com/wide/api/product/prodDesc.jsp?type=S&modelno=" + id
                res = req.urlopen(url)
                json_obj = json.load(res)
                print("http://www.enuri.com/wide/api/product/prodDesc.jsp?type=S&modelno=" + id)
        line = '''pType: GL
        idx: 0
        modelno: 78553881
        cate: 04042302
        point: 0
        isphoto:
        shopcodes:
        word_code:
        page: 1
        pagesize: 5
        '''
    # ===================================================================================
if __name__ == '__main__':
    result = enuri()
    result.prodDesc()
    print("크롤링이 완료되었습니다.")

pType=GL&idx=0&modelno=78553881&cate=04042302&point=0&isphoto=&shopcodes=&word_code=&page=1&pagesize=5