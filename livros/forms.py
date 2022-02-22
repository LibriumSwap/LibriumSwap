from django import forms
from django.forms import ModelForm

from .models import LivroAnuncio

CATEGORIA_CHOICES = (
	("V", "Venda"),
	("T", "Troca")
)

NOTA_CHOICES = [('1', '☆'),
			   ('2', '☆'),
			   ('3', '☆'),
			   ('4', '☆'),
			   ('5', '☆'),]

class NovoAnuncioForm(ModelForm):
	detalhes = forms.CharField(required=False)
	imagem1 = forms.ImageField(widget=forms.FileInput(attrs={'class': 'image-input'}))
	imagem2 = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'image-input'}))
	imagem3 = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'image-input'}))
	imagem4 = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'image-input'}))

	class Meta:
		model = LivroAnuncio
		fields = ['titulo', 'autor', 'categoria', 'preco', 'sinopse', 'detalhes']
		widgets = {
			'titulo': forms.TextInput(attrs={'class': 'effect-16'}),
			'autor': forms.TextInput(attrs={'class': 'effect-16'}),
			'categoria': forms.RadioSelect,
			'preco': forms.NumberInput(attrs={'class': 'effect-16'}),
			'sinopse': forms.Textarea(attrs={'class': 'draw meet'}),
		}

class EditarAnuncioForm(ModelForm):
	detalhes = forms.CharField(required=False)
	imagem1 = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'image-input'}))
	imagem2 = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'image-input'}))
	imagem3 = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'image-input'}))
	imagem4 = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'image-input'}))

	class Meta:
		model = LivroAnuncio
		fields = ['titulo', 'autor', 'categoria', 'preco', 'sinopse', 'detalhes']
		widgets = {
			'titulo': forms.TextInput(attrs={'class': 'effect-16 has-content'}),
			'autor': forms.TextInput(attrs={'class': 'effect-16 has-content'}),
			'categoria': forms.RadioSelect,
			'preco': forms.NumberInput(attrs={'class': 'effect-16 has-content'}),
			'sinopse': forms.Textarea(attrs={'class': 'draw meet'}),
		}

class AvaliarProdutoForm(forms.Form):
	comentario = forms.CharField(max_length=256, widget=forms.Textarea())
	nota = forms.ChoiceField(choices=NOTA_CHOICES)