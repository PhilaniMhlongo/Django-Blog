from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.urls import reverse


# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        # How you want to filter your post
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)
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