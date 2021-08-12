from django.urls import path

from . import views

urlpatterns = [
    path("anuncio/<str:id_anuncio>", views.anuncio, name="anuncio_livro"),
    path('novo/anuncio', views.novo_anuncio, name="novo_anuncio")
]