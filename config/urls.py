from django.urls import path
from . import views

urlpatterns = [
    path('settings/', views.settingsView, name="settings"),
    path('settings/privacity', views.privacityView, name="privacity"),
    path('settings/security', views.securityView, name="security"),
    path('settings/profile', views.profileView, name="profile"),
    path('settings/payment', views.paymentView, name="payment"),
    path('settings/notifications', views.notificationsView, name="notifications"),
]