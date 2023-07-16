from django.shortcuts import render,get_object_or_404
from blog.models import Post,comment
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from blog.forms import CommentForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def blog_views(request,**kwargs):    #**kwrgs=cat_name=None,author_username=None
    posts=Post.objects.filter(status=1)
    if kwargs.get('cat_name') !=None:
        posts=posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username'):
        posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('tag_name') !=None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
       


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

@csrf_exempt
def blog_single(request,pid):
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your comment submited successfully')
        else:
            messages.add_message(request,messages.ERROR,"your comment did't Submited")

    posts=Post.objects.filter(status=1)
    post=get_object_or_404(Post,pk=pid)
    comments=comment.objects.filter(post=post.id, approved=True).order_by('-created_date')
    form=CommentForm()
    contex={'post':post,'comments':comments,"form":form}
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

     
