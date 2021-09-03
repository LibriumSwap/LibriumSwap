import json
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from livros.models import LivroAnuncio

@login_required
def carrinho(request):

	if request.session.get('carrinho'):
		anuncios = LivroAnuncio.objects.filter(id__in=[anuncio_id for anuncio_id in request.session['carrinho']])
		total = anuncios.aggregate(Sum('preco'))

	return render(request, "carrinho.html", {
		"carrinho": anuncios,
		"total": total
		})

def adicionar_ao_carrinho(request):
	if request.user.is_authenticated:
		data = json.loads(request.body)
		anuncio_id = data.get('anuncio_id')

		if not request.session.get('carrinho'):
			request.session['carrinho'] = []

		request.session['carrinho'].append(anuncio_id)
		request.session.modified = True

		return JsonResponse({"success": "adicionado"})
	else:
		return JsonResponse({"error": "login"})

def remover_do_carrinho(request):
	if request.user.is_authenticated:
		data = json.loads(request.body)
		anuncio_id = data.get('anuncio_id')

		carrinho = request.session.get('carrinho')
		if anuncio_id in carrinho:
			request.session.get('carrinho').remove(anuncio_id)
		request.session.modified = True

		return JsonResponse({"success": "removido"})
	else:
		return JsonResponse({"error": "login"})