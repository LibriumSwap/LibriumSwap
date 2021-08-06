from django.db import models
from django import apps

class Livro(models.Model):
	titulo = models.CharField(max_length=128)
	autor = models.CharField(max_length=64)
	sinopse = models.TextField()
	data_publicacao = models.DateField()

class LivroVenda(models.Model):
	livro = models.ForeignKey('Livro', on_delete=models.PROTECT)
	detalhes = models.JSONField(max_length=248)
	anunciante = models.ForeignKey('autenticacao.CustomUser', on_delete=models.CASCADE)
	preco = models.FloatField(max_length=64)
	imagens = models.ManyToManyField('LivroVendaImagens')

class LivroVendaImagens(models.Model):
	imagem = models.ImageField(upload_to='anuncios')