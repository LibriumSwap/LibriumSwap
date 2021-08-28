import json
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from livros.models import LivroAnuncio

def carrinho(request):
	anuncios = []
	if request.session.get('carrinho'):
		for anuncio_id in request.session['carrinho']:
			anuncio = get_object_or_404(LivroAnuncio, id=anuncio_id)
			anuncios.append(anuncio)

	return render(request, "carrinho.html", {
		"carrinho": anuncios
		})

def adicionar_ao_carrinho(request):
	data = json.loads(request.body)
	anuncio_id = data.get('anuncio_id')

	if not request.session.get('carrinho'):
		request.session['carrinho'] = []

	request.session['carrinho'].append(anuncio_id)
	request.session.modified = True

	return JsonResponse({"success": "adicionado"})

def remover_do_carrinho(request):
	data = json.loads(request.body)
	anuncio_id = data.get('anuncio_id')

	carrinho = request.session.get('carrinho')
	if anuncio_id in carrinho:
		request.session.get('carrinho').remove(anuncio_id)
	request.session.modified = True

	return JsonResponse({"success": "removido"})