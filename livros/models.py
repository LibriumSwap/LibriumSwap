from django.db import models
from django import apps

from django.contrib.auth import get_user_model

User = get_user_model()

CATEGORIA_CHOICES = (
	("V", "Venda"),
	("T", "Troca")
)

class LivroAnuncio(models.Model):
	anunciante = models.ForeignKey(User, on_delete=models.CASCADE)
	titulo = models.CharField(max_length=128)
	autor = models.CharField(max_length=64)
	categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES, blank=False, null=False)
	preco = models.FloatField(max_length=64, blank=True, null=True)
	sinopse = models.TextField()
	detalhes = models.JSONField(max_length=248, default=dict)
	anunciado = models.BooleanField(default=True)
	imagens = models.ManyToManyField('LivroAnuncioImagem')
	avaliacoes = models.ManyToManyField('AnuncioAvaliacao')

class LivroAnuncioImagem(models.Model):
	imagem = models.ImageField(upload_to='images/anuncios')
	num = models.IntegerField()

class AnuncioAvaliacao(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	nota = models.IntegerField()
	comentario = models.CharField(max_length=256)
	data = models.DateTimeField(auto_now_add=True)

class Favorito(models.Model):
	user = models.ForeignKey(User, related_name="favorito", on_delete=models.CASCADE)
	#favoritos = models.ManyToManyField(LivroAnuncio, blank=True) 
