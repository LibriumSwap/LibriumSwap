from django.db import models
from localflavor.br.models import BRCPFField

from checkout.models import Pedido

class Pagamento(models.Model):
	pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT, blank=True, null=True)
	total = models.FloatField(null=True)
	num_cartao = models.IntegerField()
	mes_validade = models.IntegerField()
	ano_validade = models.IntegerField()
	cod_seguranca = models.IntegerField()
	titular = models.CharField(max_length=128)
	email = models.EmailField()
	cpf = BRCPFField("CPF")
	data_pagamento = models.DateTimeField(auto_now_add=True)