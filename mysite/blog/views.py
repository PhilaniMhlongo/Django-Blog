from django.shortcuts import render,get_object_or_404
from django.http import Http404
# Create your views here.

from .models import Post

def post_list(request):
    posts=Post.published.all()
    return render(request,'blog/post/list.html',{'posts':posts})


# a view to display a single post
def post_detail(request,id):
    
    # We use this to retrive the desired post
    post=get_object_or_404(Post,id=id,status=Post.Status.PUBLISHED)
    
    
    return render(request,'blog/post/details.html',{'post':post})