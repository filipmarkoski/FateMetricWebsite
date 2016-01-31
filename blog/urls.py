from django.conf.urls import url, include, patterns
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'create/$', views.post_create, name='create'),
    url(r'(?P<slug>[\w-]+)/$', views.post_detail, name='detail'), 
    #url(r'(?P<slug>[\w-]+)/updatepost/$', views.view_updatepost, name='updatepost'),
    #url(r'(?P<slug>[\w-]+)/deletepost/$', views.view_deletepost, name='deletepost'),
]