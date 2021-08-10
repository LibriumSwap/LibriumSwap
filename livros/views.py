from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import NovoAnuncioForm
from .models import Livro, LivroAnuncio, LivroAnuncioImagem
from autenticacao.models import CustomUser

def home(request):
	recentes = LivroAnuncio.objects.all().order_by('id')[:6]
	return render(request, "home/home.html", {
		"recentes": recentes
		})

def novo_anuncio(request):
	if request.method == "POST":
		form = NovoAnuncioForm(request.POST, request.FILES)
		if form.is_valid():
			titulo = form.cleaned_data["titulo"]
			autor = form.cleaned_data["autor"]
			categoria = form.cleaned_data["categoria"]
			preco = form.cleaned_data["preco"]
			sinopse = form.cleaned_data["sinopse"]
			detalhes = form.cleaned_data["detalhes"]

			user = get_object_or_404(CustomUser, username=request.user.username)

			livro_anuncio = LivroAnuncio(anunciante=user, titulo=titulo, autor=autor, categoria=categoria, preco=preco, sinopse=sinopse, detalhes=detalhes)
			livro_anuncio.save()

			imagem1 = form.cleaned_data["imagem1"]
			livro_imagem1 = LivroAnuncioImagem(imagem=imagem1)
			livro_imagem1.save()
			livro_anuncio.imagens.add(livro_imagem1)

			if form.cleaned_data["imagem2"]:
				imagem2 = form.cleaned_data["imagem2"]
				livro_imagem2 = LivroAnuncioImagem(imagem=imagem2)
				livro_imagem2.save()
				livro_anuncio.imagens.add(imagem2)
			if form.cleaned_data["imagem3"]:
				imagem1 = form.cleaned_data["imagem3"]
				livro_imagem3 = LivroAnuncioImagem(imagem=imagem3)
				livro_imagem3.save()
				livro_anuncio.imagens.add(imagem3)
			if form.cleaned_data["imagem4"]:
				imagem1 = form.cleaned_data["imagem4"]
				livro_imagem4 = LivroAnuncioImagem(imagem=imagem4)
				livro_imagem4.save()
				livro_anuncio.imagens.add(imagem4)

			livro_anuncio.save()

			return HttpResponseRedirect(reverse('home'))
		else:
			return render(request, "anuncio/novo_anuncio_form.html", {
				"form": form,
				"erros": form.errors
				})
	else:
		return render(request, "anuncio/novo_anuncio_form.html", {
			"form": NovoAnuncioForm(),
			})