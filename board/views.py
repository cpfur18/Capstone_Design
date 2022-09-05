from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from board.forms import PostForm
#from board.forms import PostForm
from board.models import Post

def comm(request):
    posts = Post.objects.all().order_by('-id') #object : ORM에서 사용되는 manage 객체 => all은 모두 가져오는 것. get은 하나.
    context = {'posts':posts}
    return render(request, "board/community.html", context)

# Create your views here.
def getpostwrite(request):
   title1 = request.POST.get("title")
   content1 = request.POST.get("content")
   context = { 'posttitle':title1, 'postcontent':content1}
   return render(request, "board/community.html", context)

def pstif(request):
    best_pstif = 1
    best_pstif_list = 2
    pstt = {'best_pstif' : best_pstif,
            'best_pstif_list' : best_pstif_list,}
    return render(request, 'board/postinfo.html', pstt)

def wrt(request):
    best_wrt = 1
    best_wrt_list = 2
    wrtt = {'best_wrt' : best_wrt,
            'best_wrt_list' : best_wrt_list,}
    return render(request, 'board/write.html', wrtt)

@login_required(login_url='/login') #로그인 유효성
def create(request):
    if request.method == "GET":
        postForm = PostForm() #만든 데이터를 딕셔너리 형태로 넘겨줌
        context = {'postForm':postForm}
        return render(request, "board/community.html", context)
    if request.method == "POST":
        postForm = PostForm(request.POST)
        if postForm.is_valid():
            post = postForm.save(commit=False)
            post.writer = request.user
            post.save()
        posts = Post.objects.all().order_by('-id') #object : ORM에서 사용되는 manage 객체 => all은 모두 가져오는 것. get은 하나.
        context = {'posts':posts}
        return render(request, "board/community.html", context)

def list(request):
    posts = Post.objects.all().order_by('-id') #object : ORM에서 사용되는 manage 객체 => all은 모두 가져오는 것. get은 하나.
    context = {'posts':posts}
    return render(request, "board/community.html", context)

def read(request, bid):
    post = Post.objects.get(id=bid)
    context = {'post': post}
    return render(request, "board/postinfo.html", context)
    #return redirect()
@login_required(login_url='/login')
def delete(request, bid):
    post = Post.objects.get(id=bid)
    if request.user != post.writer:
       return redirect('/board/read/' +str(bid))
    post.delete()
    return redirect("board/community.html")

@login_required(login_url='/login')
def update(request, bid): #html에서 actions안 달면 현재 접속한 url그대로 감
    post = Post.objects.get(id=bid)
    if request.user != post.writer:
       return redirect('/board/read/' +str(bid))
    if request.method=="GET":
        postForm = PostForm(instance=post) #조회한 내용이 입력 양식에 제대로 들어가 있는지 확인
        context = {'postForm':postForm}
        return render(request, "board/community.html", context)       
    elif request.method=="POST":
        postForm = PostForm(request.POST ,instance=post)
    if postForm.is_valid():
        post = postForm.save(commit=False)
        post.save()
    return redirect("board/community.html")