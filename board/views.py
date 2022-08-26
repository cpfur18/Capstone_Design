from django.shortcuts import render

# Create your views here.
def getpostwrite(request):
    title1 = request.POST.get("title")
    content1 = request.POST.get("content")
    context = { 'posttitle':title1, 'postcontent':content1}
    return render(request, "note_book_service/community.html", context)