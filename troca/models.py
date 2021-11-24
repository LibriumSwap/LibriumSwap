from django.db import models

from livros.models import LivroAnuncio

class LivroTroca(models.Model):
	titulo = models.CharField(max_length=128)
	autor = models.CharField(max_length=128)
	imagem = models.ImageField(upload_to='images/trocas')
	anuncio = models.ForeignKey(LivroAnuncio, on_delete=models.CASCADE)