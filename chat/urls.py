from django.conf.urls import url, include, patterns
from chat import views

urlpatterns = [
    url(r'message/$', views.message, name='message'),
    url(r'$', views.view_chat, name='chat'),
]