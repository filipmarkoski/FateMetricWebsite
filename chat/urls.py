from django.urls import path
from chat import views

urlpatterns = [
    path('message/', views.message, name='message'),
    path('', views.view_chat, name='chat'),
]