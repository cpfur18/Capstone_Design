document.addEventListener("DOMContentLoaded", function (){
    //tag 클릭 이벤트 : 테아블에서 버튼을 누르면 '선택된 태그'에 버튼 추가 또는 삭제
    //이 이벤트로 추가된 버튼은 disabled 속성이 붙어있으므로 서버에 전송되지 않음
    $(document).on("click", "input[class='btn-check col-3 tags']", function (event){
        const tagId = event.target.id + "_Selected"
        const tagName = $("label[for='" + event.target.id + "']").text()
        //표에서 태그를 클릭시 맨아래 '선택된 태그' 열에 태그 추가/삭제
        if(!event.target.checked){
            $("label[for='" + tagId + "']").remove()
            $("#"+tagId).remove()
        }else{
            $("#SelectedTags").append('<input type="checkbox" class="btn-check selectedTag col-3 tags" id="' + tagId + '" autocomplete="off" disabled>'
            + '<label class="btn col-3" for="' + tagId + '"> ' + tagName + '</label>')
        }

    })
    /*tag 클릭 이벤트2 : 원래는 선택된 태그 란에 있는 버튼을 눌러도 삭제가 되도록 했지만 form에 table을 통째로 넣어서 일단은 주석처리
    $(document).on("click", "input[class='btn-check selectedTag col-3 tags']", function (event){
        const originID = event.target.id.replace('_Selected', '')
        $("input:checkbox[id='" + originID + "']").prop("checked", false);
        $("label[for='" + event.target.id + "']").remove()
        event.target.remove()
    })
    */
    //검색 버튼 누를시 데이터 전송
    $(document).on("click", "button[id='tag_submit']", function (event){
        $.ajax({
            url: 'main:explore',
            type: 'GET',
            data: $('form').serialize(),
            success:function (){
                console.log("ajax success?")
            }
        })
    })
})