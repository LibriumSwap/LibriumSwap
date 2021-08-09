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
	preco = forms.FloatField()
	sinopse = forms.CharField(widget=forms.Textarea, required=False)
	detalhes = forms.JSONField(max_length=248, required=False)
	data_publicacao = forms.DateField(required=False)