from django.urls import path

from . import views

urlpatterns = [
    path('anuncio/<str:id_anuncio>', views.anuncio, name="anuncio_livro"),
    path('novo/anuncio', views.novo_anuncio, name="novo_anuncio"),
    path('anuncios/', views.anuncios_feitos, name="anuncios"),
    path('pesquisa/', views.pesquisa, name="pesquisa"),
    path('favorito/', views.favorito, name="favorito"),
    path('favoritos/', views.favoritos, name="favoritos"),
    path('generos/<str:generos>', views.generos, name="generos"),
    path('categorias/<str:categorias>', views.categorias, name="categorias")
]