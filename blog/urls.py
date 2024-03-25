from django.urls import path,re_path

from . import views

urlpatterns=[
    path("",views.home,name="post"),
    path('about/', views.about, name='about'),
    path('post/create',views.create_post,name='post-create'),
    
    # re_path(r"^menu_item/([0-9]{2})$",views.display_menu_item),


]