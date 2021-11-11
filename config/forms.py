from autenticacao.models import User
from django import forms

class ConfigForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['profile_image']
		exclude = ['email', 'is_funcionario', 'favoritos']
