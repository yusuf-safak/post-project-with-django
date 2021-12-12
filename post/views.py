from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import post

def postlist_view(request):
    posts = post.objects.all()
    return render(request,"posts.html",{"posts":posts})
def delete_view(request,id):
    postObj = post.objects.get(id=id)
    postObj.delete()
    return HttpResponseRedirect("/post")
def update_view(request,id):
    if(request.GET.get("title")):
        title=request.GET.get("title")
        text = request.GET.get("text")
        postObj = post.objects.get(id = id)
        postObj.title = title
        postObj.text = text
        postObj.save()
    else:
        postObj = post.objects.get(id=id)
    return render(request,"update.html",{"post":postObj})
def create_view(request):
    return render(request,"create.html",{})
    
def fillForm_view(request):
    title = request.GET.get("title")
    text = request.GET.get("text")
    post.objects.create(title = title, text = text)
    return render(request,"newPostCreated.html",{"title":title})

def detail_view(request,id):
    postObj = post.objects.get(id=id)
    return render(request,"detail.html",{"post":postObj})
# Create your views here.
