import sys
import json
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile

from .forms import NovoAnuncioForm, EditarAnuncioForm, AvaliarProdutoForm
from .models import LivroAnuncio, LivroAnuncioImagem, AnuncioAvaliacao
from autenticacao.models import User
from checkout.models import Pedido
from pagamento.models import Pagamento

def anuncio(request, id_anuncio):
	anuncio = LivroAnuncio.objects.get(id=id_anuncio)
	context = {
		"anuncio": anuncio,
		}

	if User.objects.filter(username=request.user.username, favoritos=anuncio):
		context['favorito']  = True

	if anuncio.anunciante.username == request.user.username:
		context['anunciante'] = True

	return render(request, "anuncio/anuncio.html", context)

def livros_autor(request, autor):
	anuncios = LivroAnuncio.objects.filter(autor=autor)

	return render(request, "home/livros_autor.html", {
		"anuncios": anuncios
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
	if i.mode != 'RGB':
		i = i.convert('RGB')
	i.save(thumb_io, format="JPEG", quality=90)
	thumb_io.seek(0)
	inmemory_uploaded_file = InMemoryUploadedFile(thumb_io, "ImageField", "%s.jpeg" % imagem.name.split('.')[0], "image/jpeg", sys.getsizeof(thumb_io), None)

	return inmemory_uploaded_file

@login_required
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

			for i in range(1, 5):
				if i == 1:
					# Comprimir imagem antes de salvar e adicionar em livro_anuncio
					imagem_model = LivroAnuncioImagem(imagem=nova_imagem(form.cleaned_data["imagem1"]), num=i)
					imagem_model.save()
					livro_anuncio.imagens.add(imagem_model)

				else:
					# Se houver mais imagens fazer o mesmo da primeira
					if form.cleaned_data[f"imagem{i}"]:
						imagem_model = LivroAnuncioImagem(imagem=nova_imagem(form.cleaned_data[f"imagem{i}"]), num=i)
						imagem_model.save()
						livro_anuncio.imagens.add(imagem_model)

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

def anuncios_feitos(request):
	user = get_object_or_404(User, username=request.user.username)
	anuncios = LivroAnuncio.objects.filter(anunciante=user)

	return render(request, "anuncio/anuncios.html", {
		"anuncios": anuncios
		})

def compras(request):
	user = get_object_or_404(User, username=request.user.username)
	compras = Pagamento.objects.filter(pedido__in=Pedido.objects.filter(user=user, pago=True)).order_by("-data_pagamento")


	return render(request, "anuncio/compras.html", {
		"compras": compras,
		})

def compra(request, id_compra):
	user = get_object_or_404(User, username=request.user.username)
	compra = Pagamento.objects.filter(id=id_compra, pedido__in=Pedido.objects.filter(user=user))

	return render(request, "anuncio/compra.html", {
		"compra": compra
		})

def avaliar_produto(request, id_anuncio):
	anuncio = get_object_or_404(LivroAnuncio, id=id_anuncio)

	if request.method == "GET":
		return render(request, "anuncio/avaliar_produto.html", {
			"anuncio": anuncio
			})

	if request.method == "POST":
		form = AvaliarProdutoForm(request.POST)

		if form.is_valid():
			nota = form.cleaned_data["nota"]
			comentario = form.cleaned_data["comentario"]
			user = get_object_or_404(User, username=request.user.username)

			avaliacao = AnuncioAvaliacao(nota=nota, comentario=comentario, user=user)
			avaliacao.save()

			anuncio.avaliacoes.add(avaliacao)
			anuncio.save()

			return HttpResponseRedirect(reverse('compras'))
		else:
			print(form.errors)

@require_POST
def favorito(request):
	data = json.loads(request.body)
	id_anuncio = data.get('id')

	anuncio = get_object_or_404(LivroAnuncio, id=id_anuncio)

	if request.user.is_authenticated:
		user = get_object_or_404(User, username=request.user.username)

		if User.objects.filter(username=request.user.username, favoritos=anuncio):
			user.favoritos.remove(anuncio)
			user.save()

			return JsonResponse({'success': 'removido'})

		else:
			user.favoritos.add(anuncio)
			user.save()

			return JsonResponse({'success': 'adicionado'})
	else:
		return JsonResponse({'error': 'login'})

@login_required	
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

def editar_anuncio(request, id_anuncio):
	if request.method == "POST":
		form = EditarAnuncioForm(request.POST, request.FILES)
		if form.is_valid():

			user = get_object_or_404(User, username=request.user.username)

			livro_anuncio = LivroAnuncio.objects.get(id=id_anuncio)

			livro_anuncio.titulo = form.cleaned_data["titulo"]
			livro_anuncio.autor = form.cleaned_data["autor"]
			livro_anuncio.categoria = form.cleaned_data["categoria"]
			livro_anuncio.sinopse = form.cleaned_data["sinopse"]
			livro_anuncio.detalhes = form.cleaned_data["detalhes"]

			if form.cleaned_data["categoria"] != "T":
				livro_anuncio.preco = form.cleaned_data["preco"]
			livro_anuncio.save()

			for i in range(1, 5):
				if i == 1:
					if form.cleaned_data[f"imagem{i}"]:
						imagem1 = livro_anuncio.imagens.get(num=i)
						imagem1.imagem = nova_imagem(form.cleaned_data[f"imagem{i}"])
						imagem1.save()
				else:
					if form.cleaned_data[f"imagem{i}"]:
						if livro_anuncio.imagens.filter(num=i):
							imagem = livro_anuncio.imagens.get(num=i)
							imagem.imagem = nova_imagem(form.cleaned_data[f"imagem{i}"])
							imagem.save()

						else:
							imagem_model = LivroAnuncioImagem(imagem=nova_imagem(form.cleaned_data[f"imagem{i}"]), num=i)
							imagem_model.save()
							livro_anuncio.imagens.add(imagem_model)

			livro_anuncio.save()

			return HttpResponseRedirect(reverse('home'))
		else:
			print(form.errors)

	if request.method == "GET":
		anuncio = get_object_or_404(LivroAnuncio, id=id_anuncio)

		data = {
			'titulo': anuncio.titulo,
			'autor': anuncio.autor,
			'categoria': anuncio.categoria,
			'preco': anuncio.preco,
			'sinopse': anuncio.sinopse
		}

		form = EditarAnuncioForm(initial=data)

		if request.user == anuncio.anunciante:
			return render(request, "anuncio/editar_anuncio.html", {
				"form": form,
				"anuncio": anuncio
				})

def pausar_anuncio(request, id_anuncio):
	anuncio = get_object_or_404(LivroAnuncio, id=id_anuncio)

	if request.user == anuncio.anunciante:
		if anuncio.anunciado == True:
			anuncio.anunciado = False
		else:
			anuncio.anunciado = True
			
		anuncio.save()

		return HttpResponseRedirect(reverse('anuncio_livro', args=id_anuncio))

def excluir_anuncio(request, id_anuncio):
	anuncio = get_object_or_404(LivroAnuncio, id=id_anuncio)

	if request.user == anuncio.anunciante:
		print('ok')