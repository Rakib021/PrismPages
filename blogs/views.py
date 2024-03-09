from django.shortcuts import render

from .models import Post,Category

# Create your views here.


def home(request):
    posts = Post.objects.all()[:11]
    cats = Category.objects.all()
    # print(posts)
    
    data ={
        'post':posts,
        'cats':cats
    }
    return render(request,'home.html',data)


def posts(request,url):
    post = Post.objects.get(url =url)
    cats = Category.objects.all()
    posts = Post.objects.all()
    # print(post)
    return render(request,'posts.html',{'posts':posts,'post':post,'cats':cats})


def category(request,url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request,'category.html',{'cat':cat,'posts':posts})