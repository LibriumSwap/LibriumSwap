from django import forms

CATEGORIA_CHOICES = (
	("V", "Venda"),
	("A", "Aluguel"),
	("T", "Troca")
)

class NovoAnuncioForm(forms.Form):
	imagem1 = forms.ImageField(widget=forms.FileInput(attrs={'class': 'image-input'}))
	imagem2 = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'image-input'}))
	imagem3 = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'image-input'}))
	imagem4 = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'image-input'}))
	titulo = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'effect-16'}))
	autor = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'effect-16'}))
	categoria = forms.ChoiceField(choices=CATEGORIA_CHOICES, widget=forms.RadioSelect)
	preco = forms.FloatField(required=False, widget=forms.NumberInput(attrs={'class': 'effect-16'}))
	sinopse = forms.CharField(widget=forms.Textarea(attrs={'class': 'draw meet'}), required=False)
	detalhes = forms.JSONField(max_length=248, required=False)

class EditarAnuncioForm(forms.Form):
	imagem1 = forms.ImageField(widget=forms.FileInput(attrs={'class': 'image-input'}))
	imagem2 = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'image-input'}))
	imagem3 = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'image-input'}))
	imagem4 = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'image-input'}))
	titulo = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'effect-16 has-content', 'disabled': 'true'}))
	autor = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'effect-16 has-content'}))
	categoria = forms.ChoiceField(choices=CATEGORIA_CHOICES, widget=forms.RadioSelect)
	preco = forms.FloatField(required=False, widget=forms.NumberInput(attrs={'class': 'effect-16 has-content'}))
	sinopse = forms.CharField(widget=forms.Textarea(attrs={'class': 'draw meet'}), required=False)
	detalhes = forms.JSONField(max_length=248, required=False)