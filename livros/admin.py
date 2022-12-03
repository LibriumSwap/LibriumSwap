from django.contrib import admin
from livros.models import LivroAnuncio, LivroAnuncioImagem, Favorito

admin.site.register(LivroAnuncio)
admin.site.register(LivroAnuncioImagem)
admin.site.register(Favorito)