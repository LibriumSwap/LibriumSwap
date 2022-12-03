import sys
import json
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.db.models import Q, Avg
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile

from .forms import NovoAnuncioForm, EditarAnuncioForm, AvaliarProdutoForm
from .models import LivroAnuncio, LivroAnuncioImagem, AnuncioAvaliacao, Favorito
from autenticacao.models import User
from checkout.models import Pedido
from pagamento.models import Pagamento

def anuncio(request, id_anuncio):
	anuncio = LivroAnuncio.objects.get(id=id_anuncio)
	nota = anuncio.avaliacoes.all().aggregate(Avg('nota'))


	context = {
		"anuncio": anuncio,
		"nota": nota,
		}

	# Caso seja favorito o botão de favoritar anúncio aparecerá já selecionado
	if Favorito.objects.filter(username=request.user.username, favoritos=anuncio):
		context['favorito']  = True

	# Se for anunciante as ferramentas de edição para o anúncio aparecerão
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

	# Procurar a "entrada" nos campos titulo, autor e anunciante de um anuncio
	resultados = LivroAnuncio.objects.filter(
		Q(titulo__icontains=entrada) | Q(autor__icontains=entrada) | 
		Q(anunciante__username__icontains=entrada
	))

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

	page_number = request.GET.get('page')
	if not request.GET.get('page'):
		page_number = 1

	paginator= Paginator(resultados, 20)
	page_obj = paginator.get_page(page_number)

	return render(request, "anuncio/pesquisa.html", {
		"page_obj": page_obj,
		"n_resultados": resultados.count(),
		"entrada": entrada,
		"pagina": page_number,
		"paginas": paginator.num_pages
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

		anuncio = form.save(commit=False)
		user = get_object_or_404(User, username=request.user.username)
		anuncio.anunciante = user
		anuncio.save()

		for i in range(1, 5):
			# Comprimir imagem antes de salvar e adicionar em livro_anuncio
			if form.cleaned_data[f"imagem{i}"]:
				imagem_model = LivroAnuncioImagem(imagem=nova_imagem(form.cleaned_data[f"imagem{i}"]), num=i)
				imagem_model.save()
				anuncio.imagens.add(imagem_model)

		anuncio.save()

		return redirect('anuncio_livro', id_anuncio=anuncio.id)
	else:
		return render(request, "anuncio/novo_anuncio_form.html", {
			"form": NovoAnuncioForm(),
			})

@login_required	
def anuncios_feitos(request):
	user = get_object_or_404(User, username=request.user.username)
	anuncios = LivroAnuncio.objects.filter(anunciante=user)

	return render(request, "anuncio/anuncios.html", {
		"anuncios": anuncios
		})

@login_required	
def compras(request):
	user = get_object_or_404(User, username=request.user.username)
	compras = Pagamento.objects.filter(pedido__in=Pedido.objects.filter(user=user, pago=True)).order_by("-data_pagamento")


	return render(request, "anuncio/compras.html", {
		"compras": compras,
		})

@login_required	
def compra(request, id_compra):
	user = get_object_or_404(User, username=request.user.username)
	compra = Pagamento.objects.filter(id=id_compra, pedido__in=Pedido.objects.filter(user=user))

	return render(request, "anuncio/compra.html", {
		"compra": compra
		})

@login_required	
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

			return redirect('compras')
		else:
			print(form.errors)

@require_POST
def favorito(request):
	data = json.loads(request.body)
	id_anuncio = data.get('id')

	anuncio = get_object_or_404(LivroAnuncio, id=id_anuncio)

	if request.user.is_authenticated:
		user = get_object_or_404(User, username=request.user.username)
		favorito = get_object_or_404(user=user)


		if Favorito.objects.filter(user=request.user.username, favoritos=anuncio):
			favorito.favoritos.remove(anuncio)
			favorito.save()

			return JsonResponse({'success': 'removido'})

		else:
			favorito.favoritos.add(anuncio)
			favorito.save()

			return JsonResponse({'success': 'adicionado'})
	else:
		return JsonResponse({'error': 'login'})

@login_required	
def favoritos(request):
	user = User.objects.get(username=request.user.username)
	favoritos = Favorito.objects.filter(user=user)
	

	return render(request, "anuncio/favoritos.html", {
		"favoritos": favoritos.objects.all()
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

@login_required	
def editar_anuncio(request, id_anuncio):
	anuncio = get_object_or_404(LivroAnuncio, id=id_anuncio)

	if request.user == anuncio.anunciante:
		if request.method == "POST":
			livro_anuncio = LivroAnuncio.objects.get(id=id_anuncio)
			form = EditarAnuncioForm(request.POST, request.FILES, instance=livro_anuncio)
			anuncio = form.save()

			for i in range(1, 5):
				if form.cleaned_data[f"imagem{i}"]:
					if anuncio.imagens.filter(num=i):
						imagem = livro_anuncio.imagens.get(num=i)
						imagem.imagem = nova_imagem(form.cleaned_data[f"imagem{i}"])
						imagem.save()

					else:
						imagem_model = LivroAnuncioImagem(imagem=nova_imagem(form.cleaned_data[f"imagem{i}"]), num=i)
						imagem_model.save()
						anuncio.imagens.add(imagem_model)

			anuncio.save()

			return redirect('anuncio_livro', id_anuncio=anuncio.id)

		if request.method == "GET":
			form = EditarAnuncioForm(instance=anuncio)

			return render(request, "anuncio/editar_anuncio.html", {
				"form": form,
				"anuncio": anuncio
				})
	else:
		return redirect('home')

@login_required
def pausar_anuncio(request, id_anuncio):
	anuncio = get_object_or_404(LivroAnuncio, id=id_anuncio)

	if request.user == anuncio.anunciante:
		if anuncio.anunciado == True:
			anuncio.anunciado = False
		else:
			anuncio.anunciado = True
			
		anuncio.save()

		return redirect('anuncio_livro', id_anuncio=livro_anuncio.id)
	else:
		return redirect('home')

@login_required
def excluir_anuncio(request, id_anuncio):
	anuncio = get_object_or_404(LivroAnuncio, id=id_anuncio)

	if request.user == anuncio.anunciante:
		anuncio.delete()

		return redirect('home')
	else:
		return redirect('home')