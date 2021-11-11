from django.urls import path
from . import views

urlpatterns = [
    path('settings/', views.settingsView, name="settings"),
    path('privacity', views.privacityView, name="privacity"),
    path('security', views.securityView, name="security"),
]