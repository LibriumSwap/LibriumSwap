from autenticacao.models import User
from django import forms
from checkout.models import Pedido

class ConfigForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['profile_image']
		exclude = ['email', 'is_funcionario', 'favoritos']

class CheckoutInfo(forms.ModelForm):
	class Meta:
		model = Pedido
		exclude = ['user', 'anuncio', 'nome', 'cpf']
		