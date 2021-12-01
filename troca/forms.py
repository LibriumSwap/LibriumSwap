from django import forms
from django.forms import TextInput, FileInput

from .models import LivroTroca

class LivroTrocaForm(forms.ModelForm):
	class Meta:
		model = LivroTroca
		exclude = ['anuncio', 'user']
		widgets = {
			'titulo': TextInput(attrs={'class': 'effect-16'}),
			'autor': TextInput(attrs={'class': 'effect-16'}),
			'imagem': FileInput(attrs={'class': 'image-input'})
		}