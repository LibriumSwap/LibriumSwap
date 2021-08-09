from django.shortcuts import render
from .forms import NovoAnuncioForm
from .models import Livro, LivroAnuncio, LivroVendaImagens

def home(request):
	return render(request, "home/home.html")

def novo_anuncio(request):
	if request.method == "POST":
		form = NovoAnuncioForm(request.POST, request.FILES)
		if form.is_valid():
			pass
		else:
			return render(request, "anuncio/novo_anuncio_form.html", {
				"form": form
				})
	else:
		return render(request, "anuncio/novo_anuncio_form.html", {
			"form": NovoAnuncioForm(),
			})