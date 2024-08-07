from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.urls import reverse


# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        # How you want to filter your post
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)
    
# Post Model
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT='DF','Draft'
        PUBLISHED='PB','Published'

    # Model fields

    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250,unique_for_date='publish')
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    status=models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)

    objects=models.Manager()# the default manager
    published=PublishedManager() #Our custom manager


    class Meta:
        ordering=['-publish']
        indexes=[models.Index(fields=['-publish']),]

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                        args=[self.publish.year,
                              self.publish.month,
                              self.publish.day,
                              self.slug])
    

# Comment model
#After Creating a model you have to apply migration
# python manage.py makemigrations blog
# This many-to-one relationship is defined in the Comment model because each comment will be made on one post
class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'