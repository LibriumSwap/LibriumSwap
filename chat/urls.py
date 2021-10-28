from django.urls import path
from chat.views import chatView, roomView
from . import views

urlpatterns = [
    path('', views.chatView, name="chat"),
    path('<str:other_username>/', views.roomView, name="room"),
]