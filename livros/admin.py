from django.contrib import admin
from livros.models import LivroAnuncio, LivroAnuncioImagem

admin.site.register(LivroAnuncio)
admin.site.register(LivroAnuncioImagem)