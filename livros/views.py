import sys
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from .forms import NovoAnuncioForm
from .models import Livro, LivroAnuncio, LivroAnuncioImagem
from autenticacao.models import CustomUser

def anuncio(request, id_anuncio):
	anuncio = LivroAnuncio.objects.get(id=id_anuncio)
	return render(request, "anuncio/anuncio.html", {
		"anuncio": anuncio
		})

def nova_imagem(imagem):
	i = Image.open(imagem)
	thumb_io = BytesIO()
	i = i.resize((260, 380))
	i.save(thumb_io, format="JPEG", quality=90)
	thumb_io.seek(0)
	inmemory_uploaded_file = InMemoryUploadedFile(thumb_io, "ImageField", "%s.jpeg" % imagem.name.split('.')[0], "image/jpeg", sys.getsizeof(thumb_io), None)

	imagem_model = LivroAnuncioImagem(imagem=inmemory_uploaded_file)
	imagem_model.save()
	return imagem_model

def novo_anuncio(request):
	if request.method == "POST":
		form = NovoAnuncioForm(request.POST, request.FILES)
		if form.is_valid():
			titulo = form.cleaned_data["titulo"]
			autor = form.cleaned_data["autor"]
			categoria = form.cleaned_data["categoria"]
			
				
			sinopse = form.cleaned_data["sinopse"]
			detalhes = form.cleaned_data["detalhes"]

			user = get_object_or_404(CustomUser, username=request.user.username)

			livro_anuncio = LivroAnuncio(anunciante=user, titulo=titulo, autor=autor, categoria=categoria, sinopse=sinopse, detalhes=detalhes)
			if categoria != "T":
				preco = form.cleaned_data["preco"]
				livro_anuncio.preco = preco
			livro_anuncio.save()

			# Comprimir imagem antes de salvar e adicionar em livro_anuncio
			livro_anuncio.imagens.add(nova_imagem(form.cleaned_data["imagem1"]))

			# Se houver mais imagens fazer o mesmo da primeira
			if form.cleaned_data["imagem2"]:
				livro_anuncio.imagens.add(nova_imagem(form.cleaned_data["imagem2"]))
			if form.cleaned_data["imagem3"]:
				livro_anuncio.imagens.add(nova_imagem(form.cleaned_data["imagem2"]))
			if form.cleaned_data["imagem4"]:
				livro_anuncio.imagens.add(nova_imagem(form.cleaned_data["imagem4"]))

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