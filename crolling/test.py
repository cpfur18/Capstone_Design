{% extends 'base.html' %}
{% block content %}
{% load static %}
    <!--배너-->
    <div id="template-mo-zay-hero-carousel" class="carousel slide" data-bs-ride="carousel">
        <ol class="carousel-indicators">
            <li data-bs-target="#template-mo-zay-hero-carousel" data-bs-slide-to="0" class="active"></li>
            <li data-bs-target="#template-mo-zay-hero-carousel" data-bs-slide-to="1"></li>
            <li data-bs-target="#template-mo-zay-hero-carousel" data-bs-slide-to="2"></li>
        </ol>
        <div class="carousel-inner">
            <div class="carousel-item active">
                <div class="container">
                    <div class="row p-5">
                        <div class="mx-auto col-md-8 col-lg-6 order-lg-last">
                            <img class="img-fluid" src="{% static 'test img/gp66.jpg' %}" alt="">
                        </div>
                        <div class="col-lg-6 mb-0 d-flex align-items-center">
                            <div class="text-align-left align-self-center">
                                <h1 class="h2">노트북 선택 가이드</h1>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="carousel-item">
                <div class="container">
                    <div class="row p-5">
                        <div class="mx-auto col-md-8 col-lg-6 order-lg-last">
                            <img class="img-fluid" src="{% static 'test img/legion 5i pro.jpg' %}" alt="">
                        </div>

                        <div class="col-lg-6 mb-0 d-flex align-items-center">
                            <div class="text-align-left">
                                <h1 class="h2">노트북 선택 가이드</h1>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="carousel-item">
                <div class="container">
                    <div class="row p-5">
                        <div class="mx-auto col-md-8 col-lg-6 order-lg-last">
                            <img class="img-fluid" src="{% static 'test img/legion 5 pro r7.jpg' %}" alt="">
                        </div>
                        <div class="col-lg-6 mb-0 d-flex align-items-center">
                            <div class="text-align-left">
                                <h1 class="h2">노트북 선택 가이드</h1>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!--오른쪽으로 이동-->
        <a class="carousel-control-prev text-decoration-none w-auto ps-3" href="#template-mo-zay-hero-carousel" role="button" data-bs-slide="prev">
            <i class="fas fa-chevron-left"></i>
        </a>

        <!--왼쪽으로 이동-->
        <a class="carousel-control-next text-decoration-none w-auto pe-3" href="#template-mo-zay-hero-carousel" role="button" data-bs-slide="next">
            <i class="fas fa-chevron-right"></i>
        </a>
    </div>

<!--카테고리 고르기-->
<nav class="navbar navbar-expand-lg navbar-light shadow">
    <section class="container d-flex justify-content-around align-items-center">
        <div class="align-self-center collapse navbar-collapse flex-fill  d-flex justify-content-around" id="templatemo_main_nav">
                <ul class="nav navbar-nav d-flex justify-content-around p-0">
                    <li class="nav-item mx-1">
                        <p class="text-center"><a class="nav-link text-muted h4" href="new" id="new" onclick="productListChange('new')">최신</a></p>
                    </li>
                    <li class="nav-item mx-1">
                        <p class="text-center"><a class="nav-link text-muted h4" href="popular" id="popular" onclick="productListChange('popular')">인기</a></p>
                    </li>
                    <li class="nav-item mx-1">
                        <p class="text-center"><a class="nav-link text-muted h4" href="gaming" id="gaming" onclick="productListChange('gaming')">게이밍</a></p>
                    </li>
                    <li class="nav-item mx-1">
                        <p class="text-center"><a class="nav-link text-muted h4" href="coding" id="coding" onclick="productListChange('coding')">코딩용</a></p>
                    </li>
                    <li class="nav-item mx-1">
                        <p class="text-center"><a class="nav-link text-muted h4" href="deskJob" id="deskJob" onclick="productListChange('deskJob')">사무용</a></p>
                    </li>
                    <li class="nav-item mx-1">
                        <p class="text-center"><a class="nav-link text-muted h4" href="videoEdit" id="videoEdit" onclick="productListChange('videoEdit')">영상편집</a></p>
                    </li>
                    <li class="nav-item mx-1">
                        <p class="text-center"><a class="nav-link text-muted h4" href="videoWatch" id="videoWatch" onclick="productListChange('videoWatch')">영상시청</a></p>
                    </li>
                </ul>
        </div>
    </section>
</nav>

<!--리뷰 리스트-->
<section class="container-fluid bg-light">
    <div class="row text-center">
        <div class="col-xs mt-3">
            <h1 class="h1" id="popularReviewTitle">인기 리뷰</h1>
        </div>
    </div>

    <div class="row justify-content-center">
        <!--Start Controls-->
        <div class="col-1 align-self-center text-decoration-none w-auto ps-3">
            <a href="#multi-item-review" role="button" data-bs-slide="prev">
                <i class="text-dark fas fa-chevron-left"></i>
                <span class="sr-only">Previous</span>
            </a>
        </div>
        <!--End Controls-->
        <div id="multi-item-review" class="col-10 carousel slide carousel-multi-item" data-bs-ride="carousel">
            <!--Start Slides-->
            <div class="carousel-inner product-links-wap" role="listbox">

                <!--First slide-->
                <div class="carousel-item active">
                    <div class="row justify-content-center">
                        <div class="col-lg-4 col-sm-12">
                            <div class="card mb-3 p-3">
                                <div class="row g-0">
                                        <div class="card-body">
                                            <a href="product.html" class="h4 text-decoration-none text-info">
                                                레노버 LEGION 5 Pro 16ACH R7 STORM </a>
                                            <p class="card-text">
                                                <p>
                                                    <a class="reviewTextInMain text-decoration-none text-muted" href="index.html">
                                                        내생에 첫 노트북인데 한참을 고르고 고르다가 요제품을보고 재고뜰때까지 기다렸다가 운좋게 입고일정 떠서 바로 예약했는데 실제 사용해보니 정말 빠르고 좋습니다~^^ 게이밍 노트북이라 투박하겠지 생각했는데 그레이 색상으로 세련된 디자인이라 놀랬어요특히 부팅을 하면 레노버 마크에 불이 들어와서 너무 예뻐요ㅎ화면도 크고 키보드도 전용 미디어 컨트롤을 위한 풀사이즈 키, 큰 화살표 키를 적용해 너무 편해요역시 게이밍 노트북이라 그런지 색감이 뛰어나고 실감나더라구요게임할 맛나게 하는 노트북 맞습니다!!이러한 특장점이 있는데다 가격까지 착해서 선택하지 않을 수 없었습니다.진짜 가성비 갑입니다. 게다가 1월 초에나 받을수 있을줄 알았는데 생각했던 일정보다 빨리받아서 좋아요~^^ 항상 품절인 이유가 있는거 같아요~ 기다리다기다리다 받은 만큼 기쁨도 두배인듯해요~내돈내산~ㅋㅋ 잘쓰겠습니다~많이 파세요~!!
                                                    </a>
                                                </p>
                                                #무거운 #뛰어난 #발열 #게이밍
                                            </p>
                                        </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-sm-12">
                            <div class="card mb-3 p-3">
                                <div class="row g-0">
                                        <div class="card-body">
                                            <a href="product.html" class="h4 text-decoration-none text-info">
                                                LG전자 2022 그램16(12세대) 16ZD90Q-EX76K </a>
                                            <p class="card-text">
                                                <p>
                                                    <a class="reviewTextInMain text-decoration-none text-muted" href="index.html">
                                                        휴대성과 고사양의 공존이 어렵다는 노트북에 대한 편견을 깨버린 LG그램이 한 단계 더 업그레이드되서 나왔네요. ？？？？ 코로나시국으로 노트북으로 재택근무하며 업무보는 일이 많아져 자연스레 노트북에 대해 관심이 커지고 있었는데 뉴그램 성능을 하나하나 살펴보니 어머 이건 사야해가 절로 나옵니다!! 우선 풀HD보다 2배 더 선명한 초고해상도 WQXGA가 적용된 16:10 화면비율이 시선을 훔치고, 인텔 12세대에 그램 최초 지포스 RTX 외장그래픽 탑재까지 되있어 영상작업이나 게임할 때 처리속도나 그래픽 성능면에서 파워풀한 퍼포먼스가 벌써부터 기대됩니다. 강력한 디스플레이 성능때문에 눈이 부시진 않을까 했는데 안티글레어 패널이 적용되어 빛 반사도 막아주고 눈이 전혀 피로하지 않겠더라고요. ^^ 게다가 얼굴 시선감지 기술이라니.. ㅠㅠ 이 간지폭발하는 편의성에 보안까지 맘놓을 수 있다고요!! 너무 성능이 뛰어나면 무겁거나 금방 뜨거워지진 않을까? 배터리가 금방 닳진 않을까? 걱정이 앞서기도 했지만, 역시 LG그램♥ 걱정은 기우!! 듀얼 팬쿨링으로 발열걱정 잡아주더니 1.2kg 초경량 몸무게와 90Wh 대용량배터리로 언제 어디서나 최적의 작업환경을 만들어 주네요. 그냥 백에 갖고다니다가 켜면 그 곳이 내 사무실이자 작업실이 될 것 같아요!! 카피답게 그램다운 섬세한 미니멀리즘!! 이 모든 기능을 갖고도 전혀 무겁지않고 디자인까지 완벽한 이 친구 언제 나 곁에 두고 싶은 제 베프로 삼고 싶네요.♥
                                                    </a>
                                                </p>
                                                #무거운 #뛰어난 #발열 #게이밍
                                            </p>
                                        </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-sm-12">
                            <div class="card mb-3 p-3">
                                <div class="row g-0">
                                        <div class="card-body">
                                            <a href="product.html" class="h4 text-decoration-none text-info">
                                                레노버 LEGION 5i Pro 16ITH I7 STORM 3060 </a>
                                            <p class="card-text">
                                                <p>
                                                    <a class="reviewTextInMain text-decoration-none text-muted" href="index.html">
                                                        작년 10월에 품절되서 반포기 상태였는데 갑자기 재고풀려 고민도 없이 바로 질렀습니다. 역시나 최고는 최고입니다.요즘 노트북 시장이 전체적으로 가격이 올랐는데 레노버 리전 요 녀석은 이유있는 가격상승이라 납득이 가는 몇 안돼는 랩탑중 하나 입니다.이녀석 만큼 유튜브에 리뷰 많이 된게 있나 싶을 정도로 테크유튜버들 필수 컨텐츠이죠. 물론 인텔버전이 아닌 대부분이 amd 버전이지만가장 중요한 장점은 90%이상 중첩됩니다.인텔이 그동안 삽질하므로 인해 AMD CPU가 강세였는데 타이거레이크중 지금 여기에 들어간 녀석부터 세잔을 추월했죠게다가 인텔버전은 진리의 썬더볼트 단자 지원이되어 수많은 응용 장비를 연결할수 있어서 상업용으로도 아주 제격입니다.게임용으론 말할것도 없고요. 세잔에 비해서 요놈들 GPU 오버가 됩니다. 게다가 130TGP 면 어지간한 3070하고 비빕니다.3070겜트북 가격이 대략 200초반선인데 그녀석들하고 비빌정도면 진짜 이만한 가성비가 또 있을까요?다만 아쉬운건 상판이 180도 펼쳐지지 않는 부분인데 해당사항이 없는 분들에겐 단점이 아니겠지만 데스크 공간 활용하는 분들에겐 조금 문제가 될수도 있는 부분이니 참고하세요. 디자인은 개취지만 뭐 나쁘지않습니다. 무엇보다 진정한 가성비가 모든걸 용서해줍니다.배송도 하루만에 받았습니다! 아이러브반석 흥해라!!
                                                    </a>
                                                </p>
                                                #무거운 #뛰어난 #발열 #게이밍
                                            </p>
                                        </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!--/.First slide-->

                <!--Second slide-->
                <div class="carousel-item">
                    <div class="row justify-content-center">
                        <div class="col-lg-4 col-sm-12">
                            <div class="card mb-3 p-3">
                                <div class="row g-0">
                                        <div class="card-body">
                                            <a href="product.html" class="h4 text-decoration-none text-info">
                                                레노버 LEGION 5 Pro 16ACH R7 STORM </a>
                                            <p class="card-text">
                                                <p>
                                                    <a class="reviewTextInMain text-decoration-none text-muted" href="index.html" >
                                                        내생에 첫 노트북인데 한참을 고르고 고르다가 요제품을보고 재고뜰때까지 기다렸다가 운좋게 입고일정 떠서 바로 예약했는데 실제 사용해보니 정말 빠르고 좋습니다~^^ 게이밍 노트북이라 투박하겠지 생각했는데 그레이 색상으로 세련된 디자인이라 놀랬어요특히 부팅을 하면 레노버 마크에 불이 들어와서 너무 예뻐요ㅎ화면도 크고 키보드도 전용 미디어 컨트롤을 위한 풀사이즈 키, 큰 화살표 키를 적용해 너무 편해요역시 게이밍 노트북이라 그런지 색감이 뛰어나고 실감나더라구요게임할 맛나게 하는 노트북 맞습니다!!이러한 특장점이 있는데다 가격까지 착해서 선택하지 않을 수 없었습니다.진짜 가성비 갑입니다. 게다가 1월 초에나 받을수 있을줄 알았는데 생각했던 일정보다 빨리받아서 좋아요~^^ 항상 품절인 이유가 있는거 같아요~ 기다리다기다리다 받은 만큼 기쁨도 두배인듯해요~내돈내산~ㅋㅋ 잘쓰겠습니다~많이 파세요~!!
                                                    </a>
                                                </p>
                                                #무거운 #뛰어난 #발열 #게이밍
                                            </p>
                                        </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-sm-12">
                            <div class="card mb-3 p-3">
                                <div class="row g-0">
                                        <div class="card-body">
                                            <a href="product.html" class="h4 text-decoration-none text-info">
                                                LG전자 2022 그램16(12세대) 16ZD90Q-EX76K </a>
                                            <p class="card-text">
                                                <p>
                                                    <a class="reviewTextInMain text-decoration-none text-muted" href="index.html">
                                                        휴대성과 고사양의 공존이 어렵다는 노트북에 대한 편견을 깨버린 LG그램이 한 단계 더 업그레이드되서 나왔네요. ？？？？ 코로나시국으로 노트북으로 재택근무하며 업무보는 일이 많아져 자연스레 노트북에 대해 관심이 커지고 있었는데 뉴그램 성능을 하나하나 살펴보니 어머 이건 사야해가 절로 나옵니다!! 우선 풀HD보다 2배 더 선명한 초고해상도 WQXGA가 적용된 16:10 화면비율이 시선을 훔치고, 인텔 12세대에 그램 최초 지포스 RTX 외장그래픽 탑재까지 되있어 영상작업이나 게임할 때 처리속도나 그래픽 성능면에서 파워풀한 퍼포먼스가 벌써부터 기대됩니다. 강력한 디스플레이 성능때문에 눈이 부시진 않을까 했는데 안티글레어 패널이 적용되어 빛 반사도 막아주고 눈이 전혀 피로하지 않겠더라고요. ^^ 게다가 얼굴 시선감지 기술이라니.. ㅠㅠ 이 간지폭발하는 편의성에 보안까지 맘놓을 수 있다고요!! 너무 성능이 뛰어나면 무겁거나 금방 뜨거워지진 않을까? 배터리가 금방 닳진 않을까? 걱정이 앞서기도 했지만, 역시 LG그램♥ 걱정은 기우!! 듀얼 팬쿨링으로 발열걱정 잡아주더니 1.2kg 초경량 몸무게와 90Wh 대용량배터리로 언제 어디서나 최적의 작업환경을 만들어 주네요. 그냥 백에 갖고다니다가 켜면 그 곳이 내 사무실이자 작업실이 될 것 같아요!! 카피답게 그램다운 섬세한 미니멀리즘!! 이 모든 기능을 갖고도 전혀 무겁지않고 디자인까지 완벽한 이 친구 언제 나 곁에 두고 싶은 제 베프로 삼고 싶네요.♥
                                                    </a>
                                                </p>
                                                #무거운 #뛰어난 #발열 #게이밍
                                            </p>
                                        </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-sm-12">
                            <div class="card mb-3 p-3">
                                <div class="row g-0">
                                        <div class="card-body">
                                            <a href="product.html" class="h4 text-decoration-none text-info">
                                                레노버 LEGION 5i Pro 16ITH I7 STORM 3060 </a>
                                            <p class="card-text">
                                                <p>
                                                    <a class="reviewTextInMain text-decoration-none text-muted" href="index.html">
                                                        작년 10월에 품절되서 반포기 상태였는데 갑자기 재고풀려 고민도 없이 바로 질렀습니다. 역시나 최고는 최고입니다.요즘 노트북 시장이 전체적으로 가격이 올랐는데 레노버 리전 요 녀석은 이유있는 가격상승이라 납득이 가는 몇 안돼는 랩탑중 하나 입니다.이녀석 만큼 유튜브에 리뷰 많이 된게 있나 싶을 정도로 테크유튜버들 필수 컨텐츠이죠. 물론 인텔버전이 아닌 대부분이 amd 버전이지만가장 중요한 장점은 90%이상 중첩됩니다.인텔이 그동안 삽질하므로 인해 AMD CPU가 강세였는데 타이거레이크중 지금 여기에 들어간 녀석부터 세잔을 추월했죠게다가 인텔버전은 진리의 썬더볼트 단자 지원이되어 수많은 응용 장비를 연결할수 있어서 상업용으로도 아주 제격입니다.게임용으론 말할것도 없고요. 세잔에 비해서 요놈들 GPU 오버가 됩니다. 게다가 130TGP 면 어지간한 3070하고 비빕니다.3070겜트북 가격이 대략 200초반선인데 그녀석들하고 비빌정도면 진짜 이만한 가성비가 또 있을까요?다만 아쉬운건 상판이 180도 펼쳐지지 않는 부분인데 해당사항이 없는 분들에겐 단점이 아니겠지만 데스크 공간 활용하는 분들에겐 조금 문제가 될수도 있는 부분이니 참고하세요. 디자인은 개취지만 뭐 나쁘지않습니다. 무엇보다 진정한 가성비가 모든걸 용서해줍니다.배송도 하루만에 받았습니다! 아이러브반석 흥해라!!
                                                    </a>
                                                </p>
                                                #무거운 #뛰어난 #발열 #게이밍
                                            </p>
                                        </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!--/.Second slide-->
            </div>
            <!--End Slides-->
        </div>
        <!--Start Controls-->
        <div class="col-1 align-self-center text-decoration-none w-auto pe-3">
            <a href="#multi-item-review" role="button" data-bs-slide="next">
                <i class="text-dark fas fa-chevron-right"></i>
                <span class="sr-only">Next</span>
            </a>
        </div>
        <!--End Controls-->
    </div>
</section>

<!--    상품 품목 출력-->
<section>
    <div class="container py-5">
        <div class="row text-center py-3">
            <div class="col-lg-6 m-auto">
                <h1 class="h1">TOP5</h1>
            </div>
        </div>
        <div class="row">
            <div class="col-xs">
                <div class="card mb-3">
                    <div class="row g-1">
                        {% if Prod_list %}
                            {% for Prod in Prod_list %}
                                <div class="row">
                                    <div class="col-md-4">
                                        <a href="">
                                            <img src="{% get_static_prefix %}assets/img/{{ Prod.prod_id }}.jpg" alt={{ Prod.prod_id }}, class="card-img-top">
                                        </a>
                                    </div>
                                    <div class="col-md-8">
                                        <div class="card-body">
                                            <a href="" class="h2 text-decoration-none text-dark">
                                                {{ Prod.prod_name }} </a>
                                            <p class="card-text">
                                                <br>
                                                {% for spec in Prod_list_spec %}
                                                    {% if spec.prod_id_id == Prod.prod_id %}
                                                        {% if spec.option_id == 1 %}
                                                            <p>운영체제 : {{ spec.option_title }}</p>
                                                        {% endif %}
                                                        {% if spec.option_id == 2 %}
                                                            <p>디스플레이 : {{ spec.option_title }}</p>
                                                        {% endif %}
                                                        {% if spec.option_id == 3 %}
                                                            <p>CPU : {{ spec.option_title }}</p>
                                                        {% endif %}
                                                        {% if spec.option_id == 4 %}
                                                            <p>GPU : {{ spec.option_title }}</p>
                                                        {% endif %}
                                                        {% if spec.option_id == 5 %}
                                                            <p>디스플레이 : {{ spec.option_title }}</p>
                                                        {% endif %}
                                                    {% endif %}
                                                {% endfor %}
                                                <br><br>
                                                {{ Prod.prod_reg_date }}
                                            </p>
                                            <br><br><br>
                                            <p class="text-muted"> {{ Prod.prod_price }}</p>
                                        </div>
                                    </div>
                                    <div></div>
                                </div>
                                <div class="border-top my-3"></div>
                            {% endfor %}
                        {% endif %}
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
<!-- End 가장 많이 본 상품 -->
{% endblock %}