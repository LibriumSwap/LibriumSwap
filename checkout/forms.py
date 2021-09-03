from django import forms
from autenticacao.models import EnderecoUser
from django.forms import TextInput

class CheckoutInfo(forms.ModelForm):
	class Meta:
		model = EnderecoUser
		fields = "__all__"
		widgets = {
			'nome_user': TextInput(attrs={'class': 'effect-16'}),
			'cpf': TextInput(attrs={'class': 'effect-16'}),
			'contato': TextInput(attrs={'class': 'effect-16'}),
			'cep': TextInput(attrs={'class': 'effect-16'}),
			'estado': TextInput(attrs={'class': 'effect-16'}),
			'cidade': TextInput(attrs={'class': 'effect-16'}),
			'bairro': TextInput(attrs={'class': 'effect-16'}),
			'rua': TextInput(attrs={'class': 'effect-16'}),
			'complemento': TextInput(attrs={'class': 'effect-16'}),
			'numero': TextInput(attrs={'class': 'effect-16'}),
		}
