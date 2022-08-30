function reviewTextEdit(riviewClass){
    const mainpageReview = document.getElementsByClassName(riviewClass)
    const textlength = 40
    for(var i = 0; i<mainpageReview.length; i++){
        var text = mainpageReview.item(i).innerText+""
        if(text.length > textlength){
            var textTmp = text.slice(0,textlength)+"..."
            mainpageReview.item(i).innerText = textTmp
        }
    }
}
document.addEventListener("DOMContentLoaded", function(){
    reviewTextEdit("reviewTextInMain")

    $('#summernote').summernote({
        placeholder: '내용을 입력해주세요.',
        tabsize: 10,
        height: 500,
        minHeight: 500,             // set minimum height of editor
        maxHeight: 500,             // set maximum height of editor
        lang: 'ko-KR',
        focus: true,
        toolbar: [
            ['fontname', ['fontname']],
            ['fontsize', ['fontsize']],
            ['style', ['bold', 'italic', 'underline','strikethrough', 'clear']],
            ['color', ['forecolor','color']],
            ['table', ['table']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['height', ['height']],
            ['insert',['picture','link','video']],
            ['view', ['fullscreen', 'help']]
          ],
        fontNames: ['Arial', 'Arial Black', 'Comic Sans MS', 'Courier New','맑은 고딕','궁서','굴림체','굴림','돋움체','바탕체'],
        fontSizes: ['8','9','10','11','12','14','16','18','20','22','24','28','30','36','50','72']

    });
    $('.note-resizebar').css('display','none');
    $('.dropdown-toggle').dropdown()

    /* 무한스크롤
    var infinite = new Waypoint.Infinite({
        element: $('.infinite-container')[0],
        offset: 'bottom-in-view',
        onBeforePageLoad: function (){
            $('.spinner-border').show();
        },
        onAfterPageLoad: function (){
            $('.spinner-border').hide();
        }
    })
    */
    //navbar를
    $(".sticky-top").css(
        "background", "white"
    )
});