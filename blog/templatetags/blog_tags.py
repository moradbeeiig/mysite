from django import template
from blog.models import Post,comment
from blog.models import Category

register=template.Library()

@register.simple_tag(name='totalposts')
def function():
    posts=Post.objects.filter(status=1).count()
    return posts


@register.simple_tag(name='comments_count')
def function(pid):
    post=Post.objects.get(pk=pid)
    comments=comment.objects.filter(post=post.id, approved=True).count()
    return comments

@register.simple_tag(name='posts')
def function():
    posts=Post.objects.filter(status=1)
    return posts

@register.filter
def snippet(value,arg=20):
    return value[:arg]

@register.inclusion_tag('blog/blog-popular-posts.html')
def latestposts(arg=3):
    posts=Post.objects.filter(status=1).order_by('publish_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts=Post.objects.filter(status=1)
    categoies=Category.objects.all()
    cat_dict={}
    for name in categoies:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}