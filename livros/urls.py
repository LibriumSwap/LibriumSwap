from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('anuncio/novo', views.novo_anuncio, name="novo_anuncio")
]