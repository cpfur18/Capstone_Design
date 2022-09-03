//index 페이지의 모바일 화면에서 navbar에 추가
document.addEventListener("DOMContentLoaded", function(){
    const index_nav
        = '  <section class="d-flex justify-content-center align-items-center d-block d-lg-none">' +
        '        <table class="align-self-center collapse navbar-collapse d-flex row justify-content-center table table-borderless border-top border-bottom" id="templatemo_main_nav">' +
        '           <tr class="d-flex justify-content-around">' +
        '               <td class="nav-item flex-fill"><a class="nav-link text-success h5 text-center" href="new" id="new">최신</a></td>' +
        '               <td class="nav-item flex-fill"><a class="nav-link text-success h5 text-center" href="gaming" id="gaming">게이밍</a></td>' +
        '           </tr>' +
        '           <tr class="d-flex justify-content-around">' +
        '               <td class="nav-item flex-fill"><a class="nav-link text-success h5 text-center" href="coding" id="coding">코딩용</a></td>' +
        '               <td class="nav-item flex-fill"><a class="nav-link text-success h5 text-center" href="deskJob" id="deskJob">사무용</a></td>' +
        '           </tr>' +
        '           <tr class="d-flex justify-content-around">' +
        '               <td class="nav-item flex-fill"><a class="nav-link text-success h5 text-center" href="videoEdit" id="videoEdit">영상편집</a></td>' +
        '               <td class="nav-item flex-fill"><a class="nav-link text-success h5 text-center" href="videoWatch" id="videoWatch">영상시청</a></td>' +
        '           </tr>' +
        '        </table>' +
        '    </section>' +
    $('#nv').after(index_nav)

    $(window).scroll(function() {
        var scrollHeight = $(window).scrollTop() + $(window).height();
        var documentHeight = $(document).height();

        if (scrollHeight + 300 >= documentHeight){
                $.ajax({
                url: "/rest/1/pages/245", // 클라이언트가 HTTP 요청을 보낼 서버의 URL 주소
                data: { name: "홍길동" },  // HTTP 요청과 함께 서버로 보낼 데이터
                method: "GET",   // HTTP 요청 메소드(GET, POST 등)
                dataType: "json" // 서버에서 보내줄 데이터의 타입
            })
        }
    });
    /*
    var infinite = new Waypoint.Infinite({
        element: $('.infinite-container')[0],
        offset: 'bottom-in-view',
        onBeforePageLoad: function (){
            $('.spinner-border').show();
        },
        onAfterPageLoad: function (){
            $('.spinner-border').hide();
        }
    })*/
});