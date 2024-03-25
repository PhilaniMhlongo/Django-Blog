from django.urls import path,re_path

from . import views

urlpatterns=[
    path("",views.home,name="post"),
    path('about/', views.about, name='about'),
    
    # re_path(r"^menu_item/([0-9]{2})$",views.display_menu_item),


]