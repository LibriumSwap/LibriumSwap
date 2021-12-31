from django.db import models
from localflavor.br.models import BRCPFField

from checkout.models import Pedido

class Pagamento(models.Model):
	pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT, blank=True, null=True)
	total = models.FloatField(null=True)
	data_pagamento = models.DateTimeField(auto_now_add=True)