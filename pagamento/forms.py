from django import forms
from django.forms import TextInput

from .models import Pagamento
from checkout.models import Pedido

class PagamentoForm(forms.ModelForm):
	class Meta:
		model = Pagamento
		exclude = ['pedido', 'total', 'data_pagamento']
		widgets = {
			'num_cartao': TextInput(attrs={'class': 'effect-19'}),
			'mes_validade': TextInput(attrs={'class': 'effect-19'}),
			'ano_validade': TextInput(attrs={'class': 'effect-19'}),
			'cod_seguranca': TextInput(attrs={'class': 'effect-19'}),
			'titular': TextInput(attrs={'class': 'effect-19'}),
			'email': TextInput(attrs={'class': 'effect-19'}),
			'cpf': TextInput(attrs={'class': 'effect-19', 'id': "cpf_mask"}),
		}