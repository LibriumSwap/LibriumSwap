from django.urls import path

from . import views

urlpatterns = [
    path('anuncio/<str:id_anuncio>', views.anuncio, name="anuncio_livro"),
    path('novo/anuncio', views.novo_anuncio, name="novo_anuncio"),
    path('anuncios/', views.anuncios_feitos, name="anuncios"),
    path('anuncio/<str:id_anuncio>/editar', views.editar_anuncio, name="editar_anuncio"),
    path('anuncio/<str:id_anuncio>/pausar', views.pausar_anuncio, name="pausar_anuncio"),
    path('anuncio/<str:id_anuncio>/excluir', views.excluir_anuncio, name="excluir_anuncio"),
    path('pesquisa/', views.pesquisa, name="pesquisa"),
    path('favorito/', views.favorito, name="favorito"),
    path('favoritos/', views.favoritos, name="favoritos"),
    path('compras/', views.compras, name="compras"),
    path('compra/<str:id_compra>', views.compra, name="compra"),
    path('generos/<str:generos>', views.generos, name="generos"),
    path('categorias/<str:categorias>', views.categorias, name="categorias")
]