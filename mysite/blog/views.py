from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
# Create your views here.

from .models import Post, Comment

def post_list(request):
    posts=Post.published.all()
    
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    posts=paginator.page(page_number)
    return render(request,'blog/post/list.html',{'posts':posts})


# a view to display a single post
def post_detail(request,year,month,day,post):
    
    # We use this to retrive the desired post
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    # Form for users to comment
    form = CommentForm()

    return render(request,
                  'blog/post/details.html',
                  {'post': post,
                   'comments': comments,
                   'form': form})

    
    return render(request,'blog/post/details.html',{'post':post})

class PostListView(ListView):
    """
    Alternative post list view
    """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
    if request.method == 'POST':
    # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
    # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read "f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'mhlongophilani04@gmail.com',[cd['to']])
            sent = True
    # ... send email
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
    'form': form,'sent': sent})



@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, \
                                   status=Post.Status.PUBLISHED)
    comment = None
    # A comment was posted
    form = CommentForm(data=request.POST)
    if form.is_valid():
        # Create a Comment object without saving it to the database
        comment = form.save(commit=False)
        # Assign the post to the comment
        comment.post = post
        # Save the comment to the database
        comment.save()
    return render(request, 'blog/post/comment.html',
                           {'post': post,
                            'form': form,
                            'comment': comment})