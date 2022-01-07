from django.db import models
from django import apps

from django.contrib.auth import get_user_model

User = get_user_model()

CATEGORIA_CHOICES = (
	("V", "Venda"),
	("A", "Aluguel"),
	("T", "Troca")
)

class Livro(models.Model):
	titulo = models.CharField(max_length=128)
	autor = models.CharField(max_length=64)

class LivroAnuncio(models.Model):
	livro = models.ForeignKey('Livro', on_delete=models.PROTECT, blank=True, null=True)
	detalhes = models.JSONField(max_length=248, default=dict)
	categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES, blank=False, null=False)
	anunciante = models.ForeignKey(User, on_delete=models.CASCADE)
	preco = models.FloatField(max_length=64, blank=True, null=True)
	imagens = models.ManyToManyField('LivroAnuncioImagem')
	titulo = models.CharField(max_length=128)
	autor = models.CharField(max_length=64)
	sinopse = models.TextField()

class LivroAnuncioImagem(models.Model):
	imagem = models.ImageField(upload_to='images/anuncios')
	num = models.IntegerField()