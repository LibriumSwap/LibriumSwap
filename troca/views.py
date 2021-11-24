from django.shortcuts import render

from .models import LivroTroca
from livros.models import LivroAnuncio
from .forms import LivroTrocaForm

def troca(request, anuncio_id):
	if request.method == "POST":
		form = LivroTrocaForm(request.POST, request.FILES)
		if form.is_valid():
			livro_troca = form.save(commit=False)
			livro_troca.anuncio = LivroAnuncio.objects.get(id=anuncio_id)
			livro_troca.save()

			print('salvo')

	if request.method == "GET":
		return render(request, "troca_form.html", {
			'form': LivroTrocaForm(),
			'anuncio_id': anuncio_id
			})