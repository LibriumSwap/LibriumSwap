from django.urls import path

from . import views

urlpatterns = [
    path("anuncio/<str:id_anuncio>", views.anuncio, name="anuncio_livro"),
    path('anuncio/novo', views.novo_anuncio, name="novo_anuncio")
]