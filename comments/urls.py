from django.urls import path
from django.contrib import admin
from comments import views

urlpatterns = [
    path('<int:id>', views.comment_thread, name='thread'),
    path('<int:id>/delete', views.comment_delete, name='thread_delete'),
]