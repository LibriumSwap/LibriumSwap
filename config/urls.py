from django.urls import path
from . import views

urlpatterns = [
    path('settings/', views.settingsView, name="settings"),
    path('settings/my-account/privacity', views.privacityView, name="privacity"),
    path('settings/my-account/security', views.securityView, name="security"),
    path('settings/my-account/profile', views.profileView, name="profile"),
    path('settings/my-account/payment', views.paymentView, name="payment"),
    path('settings/my-account/notifications', views.notificationsView, name="notifications"),
    path('settings/my-account/payment/new-payment/', views.newPaymentView, name="new-payment"),
]