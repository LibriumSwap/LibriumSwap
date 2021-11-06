from django import forms
from django.forms import TextInput, NumberInput

from .models import Pedido

class CheckoutInfo(forms.ModelForm):
	class Meta:
		model = Pedido
		exclude = ['user', 'anuncio']
		widgets = {
			'nome': TextInput(attrs={'class': 'effect-19'}),
			'cpf': TextInput(attrs={'class': 'effect-19', 'id': "cpf_mask"}),
			'contato': NumberInput(attrs={'class': 'effect-19', 'type': 'number'}),
			'cep': TextInput(attrs={'class': 'effect-19 cep', 'id': "cep_mask"}),
			'estado': TextInput(attrs={'class': 'effect-19 input-regiao'}),
			'cidade': TextInput(attrs={'class': 'effect-19 input-regiao'}),
			'bairro': TextInput(attrs={'class': 'effect-19 input-regiao'}),
			'rua': TextInput(attrs={'class': 'effect-19 input-regiao'}),
			'complemento': TextInput(attrs={'class': 'effect-19'}),
			'numero': TextInput(attrs={'class': 'effect-19', 'type': 'number'}),
		}
