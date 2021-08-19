from django.urls import path

from . import views

urlpatterns = [
    path('anuncio/<str:id_anuncio>', views.anuncio, name="anuncio_livro"),
    path('novo/anuncio', views.novo_anuncio, name="novo_anuncio"),
    path('pesquisa/', views.pesquisa, name="pesquisa"),
    path('favorito/', views.favorito, name="favorito"),
    path('favoritos/', views.favoritos, name="favoritos")
]