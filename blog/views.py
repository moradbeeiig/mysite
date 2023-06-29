from django.shortcuts import render,get_object_or_404
from blog.models import Post

# Create your views here.
def blog_views(request):
    posts=Post.objects.filter(status=1)
    contex={'posts':posts}
    return render(request,'blog/blog-home.html',contex)

def blog_single(request,pid):
        posts=Post.objects.filter(status=1)
        post=get_object_or_404(Post,pk=pid)
        contex={'post':post}
        return render (request,'blog/blog-single.html',contex)

def test(request):
    # post=get_object_or_404(Post,pk=pid)
    # contex={'post':post}
    return render(request,'test.html')
