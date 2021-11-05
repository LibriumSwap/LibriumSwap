from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class Pedido(models.Model):
	anuncio = models.ManyToManyField("livros.LivroAnuncio")
	user = models.ForeignKey(User, on_delete=models.CASCADE)
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
	pago = models.BooleanField(default=False)