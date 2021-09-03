from django import forms
from autenticacao.models import EnderecoUser
from django.forms import TextInput

class CheckoutInfo(forms.ModelForm):
	class Meta:
		model = EnderecoUser
		fields = "__all__"
		widgets = {
			'nome_user': TextInput(attrs={'class': 'effect-19'}),
			'cpf': TextInput(attrs={'class': 'effect-19', 'type': 'number'}),
			'contato': TextInput(attrs={'class': 'effect-19', 'type': 'number'}),
			'cep': TextInput(attrs={'class': 'effect-19 cep', 'type': 'number'}),
			'estado': TextInput(attrs={'class': 'effect-19'}),
			'cidade': TextInput(attrs={'class': 'effect-19'}),
			'bairro': TextInput(attrs={'class': 'effect-19'}),
			'rua': TextInput(attrs={'class': 'effect-19'}),
			'complemento': TextInput(attrs={'class': 'effect-19'}),
			'numero': TextInput(attrs={'class': 'effect-19', 'type': 'number'}),
		}
