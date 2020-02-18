from django.urls import path
from main import views

urlpatterns = [
    path('', views.view_homepage, name=''),
    path('about', views.view_aboutpage, name='about'),
    path('dislike/', views.view_dislike, name='dislike'),
    path('like/', views.view_like, name='like'),
    path('contact/', views.view_contact, name='contact'),
    # Doesn't work url(r'(?P<slug>[\w-]+)/like/$', views.post_like, name='like'),
    # path(r'contact/$', views.view_contactpage, name='contact'),
]
