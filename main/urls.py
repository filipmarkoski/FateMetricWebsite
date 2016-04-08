from django.conf.urls import url, include, patterns
from main import views

urlpatterns = [
    url(r'^$', views.view_homepage, name=''),
    url(r'about/$', views.view_aboutpage, name='about'),
    url(r'dislike/$', views.view_dislike, name='dislike'),
	url(r'like/$', views.view_like, name='like'),
    url(r'contact/$', views.view_contact, name='contact'),
    #Doestn't work url(r'(?P<slug>[\w-]+)/like/$', views.post_like, name='like'),
    #url(r'contact/$', views.view_contactpage, name='contact'),
]