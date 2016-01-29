from django.conf.urls import url, include, patterns
from main import views

urlpatterns = [
    url(r'^$', views.view_homepage, name=''),
    url(r'about/$', views.view_aboutpage, name='about'),
    url(r'contact/$', views.view_contactpage, name='contact'),
]