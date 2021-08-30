import sys
import json
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db.models import Q
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from .forms import NovoAnuncioForm
from .models import Livro, LivroAnuncio, LivroAnuncioImagem
from autenticacao.models import User

def anuncio(request, id_anuncio):
	anuncio = LivroAnuncio.objects.get(id=id_anuncio)

	if User.objects.filter(username=request.user.username, favoritos=anuncio):
		return render(request, "anuncio/anuncio.html", {
		"anuncio": anuncio,
		"favorito": True
		})
	return render(request, "anuncio/anuncio.html", {
		"anuncio": anuncio
		})


def pesquisa(request):
	entrada = request.GET.get('q')
	resultados = LivroAnuncio.objects.filter(Q(titulo__icontains=entrada) | Q(autor__icontains=entrada) | Q(anunciante__username__icontains=entrada))

	if request.GET.get('categoria'):
		resultados = resultados.filter(categoria=request.GET.get('categoria')[0].upper())

	if request.GET.get('preco_min'):
		resultados = resultados.filter(preco__gte=request.GET.get('preco_min'))
	if request.GET.get('preco_max'):
		resultados = resultados.filter(preco__lte=request.GET.get('preco_max'))

	if request.GET.get('order') == 'min_preco':
		resultados = resultados.order_by('preco')
	if request.GET.get('order') == 'max_preco':
		resultados = resultados.order_by('-preco')
	if request.GET.get('order') == 'recentes':
		resultados = resultados.order_by('-id')

	if request.GET.get('genero'):
		resultados = resultados.filter(detalhes__gênero=request.GET.get('genero'))

	return render(request, "anuncio/pesquisa.html", {
		"resultados": resultados,
		"n_resultados": resultados.count(),
		"entrada": entrada
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

			# Criar uma variável para cada valor do formulário
			titulo = form.cleaned_data["titulo"]
			autor = form.cleaned_data["autor"]
			categoria = form.cleaned_data["categoria"]
			
				
			sinopse = form.cleaned_data["sinopse"]
			detalhes = form.cleaned_data["detalhes"]

			user = get_object_or_404(User, username=request.user.username)

			livro_anuncio = LivroAnuncio(anunciante=user, titulo=titulo, autor=autor, categoria=categoria, sinopse=sinopse, detalhes=detalhes)

			# Caso a categoria seja troca o preço não precisa ser inserido
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
			# Retornar erros em caso de erro
			return render(request, "anuncio/novo_anuncio_form.html", {
				"form": form,
				"erros": form.errors
				})
	else:
		return render(request, "anuncio/novo_anuncio_form.html", {
			"form": NovoAnuncioForm(),
			})


def favorito(request):
	user = get_object_or_404(User, username=request.user.username)

	if request.method == "POST":
		data = json.loads(request.body)
		id_anuncio = data.get('id')

		anuncio = get_object_or_404(LivroAnuncio, id=id_anuncio)

		if User.objects.filter(username=request.user.username, favoritos=anuncio):
			user.favoritos.remove(anuncio)
			user.save()

			return JsonResponse({'success': 'removido'})

		else:
			user.favoritos.add(anuncio)
			user.save()

			return JsonResponse({'success': 'adicionado'})
		
def favoritos(request):
	user = User.objects.get(username=request.user.username)

	return render(request, "anuncio/favoritos.html", {
		"favoritos": user.favoritos.all()
		})


def generos(request, generos):
	anuncios = LivroAnuncio.objects.filter(detalhes__gênero__icontains=generos.lower())
	return render(request, "home/generos.html", {
		"gênero": generos,
		"anuncios": anuncios
		})


def categorias(request, categorias):
	anuncios = LivroAnuncio.objects.filter(categoria=categorias[0].upper())

	return render(request, "home/categorias.html", {
		"categoria": categorias,
		"anuncios": anuncios
		})
