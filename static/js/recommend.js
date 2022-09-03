document.addEventListener("DOMContentLoaded", function(){
    //추천 질문 답변 이벤트
    let purpose = ''
    $(document).on("click", "input[class='btn-check rec_q']", function (event){
        const ansName = event.target.name
        const ansId = event.target.id
        const ans = $("label[for='" + ansId + "']").text()
        const btnId = ansName + "_selected"

        //'나의 답변' 에 이미 있는 것은 제거
        $("#"+btnId).remove()
        //'나의 답변' 에 고른 답변을 추가
        $("#req_selected").append(''
            + '<button class="btn btn-lg rounded-pill text-white bg-success disabled my-1 align-items-center" id="' + btnId + '" style="display: block">' + ans + '</button>')
        //다른 질문 display
        if(ansName === '용도'){
            purpose = ansId
            $('#pp').css("display", "none")
            $('#prc').css("display", "grid")
        }else if(ansName === '예산'){
            $('#prc').css("display", "none")
            switch (purpose) {
                case 'pp-4': //용도-영상 편집
                    $('#ve_1').css("display", "grid")
                    break
                default:
                    $('#dsp_1').css("display", "grid")
                    break
            }
        }else if(ansName === '영상편집_화질'){
            $('#ve_1').css("display", "none")
            $('#dsp_1').css("display", "grid")
            //$('#ve_2').css("display", "grid")
        /*}else if(ansName === '영상편집_툴'){
            $('#ve_2').css("display", "none")
            $('#dsp_1').css("display", "grid")*/
        }else if(ansName === '디스플레이_색감'){
            $('#dsp_1').css("display", "none")
            $('#ptb').css("display", "grid")
        }else if(ansName === '휴대성'){
            $('#ptb').css("display", "none")
            $('#dsp_2').css("display", "grid")
        }else if(ansName === '디스플레이_크기'){
            $('#dsp_2').css("display", "none")
            $('#cp').css("display", "grid")
        }else if(ansName === '제조사'){//마지막 버튼 클릭시에 추천받기 버튼 활성화
            $('#rec_submit').attr("disabled", false)
        }


    })
    $(document).on("click", "button[id='rec_reset']", function (event){
        //질문 리셋
        $('.rec_q').prop('checked', false)
        $("#req_selected").empty() //'나의 답변'에 있는 모든 버튼 삭제
        $('#rec_submit').attr("disabled", true) //추천 받기 버튼 비활성화
        purpose = ''
        //$('#g_1').css("display", "none")
        //$('#g_2').css("display", "none")
        $('#ve_1').css("display", "none")
        //$('#ve_2').css("display", "none")
        $('#dsp_1').css("display", "none")
        $('#ptb').css("display", "none")
        $('#dsp_2').css("display", "none")
        $('#prc').css("display", "none")
        $('#cp').css("display", "none")
        $('#pp').css("display", "grid")

    })
});