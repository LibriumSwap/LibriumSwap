from django.db import models
from localflavor.br.models import BRCPFField, BRPostalCodeField, BRStateField

from django.contrib.auth import get_user_model

User = get_user_model()

class Pedido(models.Model):
	anuncio = models.ManyToManyField("livros.LivroAnuncio")
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	nome = models.CharField(max_length=128)
	cpf = BRCPFField("CPF")
	contato = models.CharField(max_length=18)
	cep = BRPostalCodeField("CEP")
	estado = BRStateField("Estado")
	cidade = models.CharField(max_length=64)
	bairro = models.CharField(max_length=64)
	rua = models.CharField(max_length=128)
	complemento = models.CharField(max_length=128, blank=True)
	numero = models.CharField(max_length=10)