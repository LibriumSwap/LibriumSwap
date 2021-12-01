from django.shortcuts import render, redirect

from .models import LivroTroca
from livros.models import LivroAnuncio
from .forms import LivroTrocaForm

from django.contrib.auth import get_user_model

User = get_user_model()

def troca(request, anuncio_id):
	if request.method == "POST":
		form = LivroTrocaForm(request.POST, request.FILES)
		if form.is_valid():
			livro_troca = form.save(commit=False)
			livro_troca.anuncio = LivroAnuncio.objects.get(id=anuncio_id)
			livro_troca.user = User.objects.get(username=request.user.username)
			livro_troca.save()

			return redirect('trocas_solicitadas')

	if request.method == "GET":
		return render(request, "troca_form.html", {
			'form': LivroTrocaForm(),
			'anuncio_id': anuncio_id
			})

def trocas_solicitadas(request):
	user = User.objects.get(username=request.user.username)
	trocas_solicitadas = LivroTroca.objects.filter(user=user)

	return render(request, "trocas_solicitadas.html", {
		"trocas_solicitadas": trocas_solicitadas
		})

def trocas_recebidas(request):
	user = User.objects.get(username=request.user.username)
	anuncios_feitos = LivroAnuncio.objects.filter(user=user)
	trocas_recebidas = LivroTroca.objects.filter(anuncio__in=anuncios_feitos)

	return render(request, "trocas_recebidas.html", {
		"trocas_recebidas": trocas_recebidas
		})