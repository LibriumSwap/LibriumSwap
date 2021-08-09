from django.db import models
from django import apps

CATEGORIA_CHOICES = (
	("V", "Venda"),
	("A", "Aluguel"),
	("T", "Troca")
)

class Livro(models.Model):
	titulo = models.CharField(max_length=128)
	autor = models.CharField(max_length=64)

class LivroAnuncio(models.Model):
	livro = models.ForeignKey('Livro', on_delete=models.PROTECT)
	detalhes = models.JSONField(max_length=248, blank=True)
	categoria = models.CharField(max_length=1, choices=CATEGORIA_CHOICES, blank=False, null=False)
	anunciante = models.ForeignKey('autenticacao.CustomUser', on_delete=models.CASCADE)
	preco = models.FloatField(max_length=64)
	imagens = models.ManyToManyField('LivroVendaImagens')
	titulo = models.CharField(max_length=128)
	autor = models.CharField(max_length=64)
	sinopse = models.TextField()
	data_publicacao = models.DateField(blank=True)

class LivroVendaImagens(models.Model):
	imagem = models.ImageField(upload_to='anuncios')