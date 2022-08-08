function productListChange(id){
    var title = document.getElementById(id).innerText
    document.getElementById("productListTitle").innerText = title+" TOP 5"
}
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
window.onload = function(){
    reviewTextEdit("reviewTextInMain")
}
//2번째 슬라이드부터 적용이 제대로 되지 않으므로 임시로 첫번째 슬라이드만 적용