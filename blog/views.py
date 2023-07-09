from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
def blog_views(request,**kwargs):    #**kwrgs=cat_name=None,author_username=None
    posts=Post.objects.filter(status=1)
    if kwargs.get('cat_name') !=None:
        posts=posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username'):
        posts = posts.filter(author__username = kwargs['author_username'])

    posts=Paginator(posts,3)
    try:
        page_number=request.GET.get('page')
        posts=posts.get_page(page_number)
    except PageNotAnInteger:
        posts=posts.get_page(1)
    except EmptyPage:
        posts=posts.get_page(1)      
    contex={'posts':posts}
    return render(request,'blog/blog-home.html',contex)

def blog_single(request,pid):
        posts=Post.objects.filter(status=1)
        post=get_object_or_404(Post,pk=pid)
        contex={'post':post}
        return render (request,'blog/blog-single.html',contex)

# def test(request):
    # post=get_object_or_404(Post,pk=pid)
    # contex={'post':post}
    # return render(request,'test.html')

def blog_category(request,cat_name):
     posts=Post.objects.filter(status=1)
     posts=posts.filter(category__name=cat_name)
     contex={'posts':posts}
     return render(request,'blog/blog-home.html',contex)

def blog_search(request):
    posts=Post.objects.filter(status=1)
    if request.method=='GET':
        if s:= request.GET.get('s'):
            posts=posts.filter(content__contains=s)
    contex={'posts':posts}
    return render(request,'blog/blog-home.html',contex)

     
