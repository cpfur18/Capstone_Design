### Django, PostgreSQL, Bootstrap 5로 만든 노트북 추천 웹서비스 입니다.
## 큐레이션, 커뮤니티, 직접탐색 기능 구현 중 입니다.

내부 서버 URL은 http://127.0.0.1:8000/ 입니다.

![3번 이미지](https://user-images.githubusercontent.com/65838532/188205727-b45a8859-a47e-4b3e-833d-93be8f255fa3.png)
1. Python selenium bs4를 사용하여 에누리(종합쇼핑몰)에서 노트북 정보 크롤링
2. Django ORM을 이용해 DB 저장
3. 수집한 정보를 바탕으로 노트북 스펙 수치화 및 태그화
4-1. 큐레이션을 통해 사용자 성향 수집 후 노트북 추천
4-2. 직접탐색 기능을 통해 노트북 정보 출력
