from django.urls import path
from django.contrib import admin
from blog import views
from blog.views import post_update

urlpatterns = [
    path('create/', views.post_create, name='create'),
    path('<slug:slug>/update/', views.post_update, name='update'),
    path('<slug:slug>/delete/', views.post_delete, name='delete'),
    path('<slug:slug>/', views.post_detail, name='detail'),
]
