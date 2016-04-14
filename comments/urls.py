from django.conf.urls import url, include, patterns
from django.contrib import admin
from comments import views

urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.comment_thread, name='thread'),
]