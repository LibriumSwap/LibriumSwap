from django.db import models

class Pedido(models.Model):
	anuncio = models.ManyToManyField("livros.LivroAnuncio")
	nome = models.CharField(max_length=128)
	cpf = models.CharField(max_length=18)
	contato = models.CharField(max_length=18)
	cep = models.CharField(max_length=8)
	estado = models.CharField(max_length=2)
	cidade = models.CharField(max_length=64)
	bairro = models.CharField(max_length=64)
	rua = models.CharField(max_length=128)
	complemento = models.CharField(max_length=128, blank=True)
	numero = models.CharField(max_length=10)