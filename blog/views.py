from django.shortcuts import render,redirect

from django.http import HttpResponse

from .models import Post

from .forms import PostForm

# Create your views here.



def home(request):
    posts=Post.objects.all()
    context={
       'posts':posts,
       'title': 'Software Bytes'
    }
    return render(request,'blog/home.html',context)


def about(request):
    return render(request,'blog/about.html')

def create_post(request):
    if request.method=='GET':
        context={'form':PostForm()}
        return render(request,'blog/post_form.html',context)
    
    elif request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog/home.html')
        
        else:
            return render(request,'blog/post_form.html',{'form':form})
