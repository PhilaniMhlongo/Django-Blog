# We created this file
# We are adding URL pattern for our views

from django.urls import path
from . import views

app_name='blog'

urlpatterns=[
    # post views
    # you can use re_path()
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
    
]