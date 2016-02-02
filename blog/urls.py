from django.conf.urls import url, include, patterns
from django.contrib import admin
from blog import views
from blog.views import post_update
urlpatterns = [
    url(r'create/$', views.post_create, name='create'), 
    url(r'(?P<slug>[\w-]+)/update/$', views.post_update, name='update'),
    url(r'(?P<slug>[\w-]+)/delete/$', views.post_delete, name='delete'),
    url(r'(?P<slug>[\w-]+)/$', views.post_detail, name='detail'),
]