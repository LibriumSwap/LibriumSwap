from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Sum

from livros.models import LivroAnuncio
from autenticacao.models import User
from .forms import CheckoutInfo

@login_required
def checkout(request, anuncio_id):
	if request.method == "GET":
		form = CheckoutInfo()
		anuncios = []
		anuncio = get_object_or_404(LivroAnuncio, id=anuncio_id)
		total = {'preco__sum': anuncio.preco}

		anuncios.append(anuncio)

		return render(request, "checkout/checkout_info.html", {
			"form": form,
			"anuncios": anuncios,
			"total": total,
			"url": "checkout",
			"id": anuncios[0].id
			})

	if request.method == "POST":
		form = CheckoutInfo(request.POST)
		anuncio = get_object_or_404(LivroAnuncio, id=anuncio_id)
		user = get_object_or_404(User, username=request.user.username)

		if form.is_valid():
			pedido = form.save(commit=False)
			pedido.user = user
			pedido.save()
			pedido.anuncio.add(anuncio)
			pedido.save()

			request.session['pedido'] = pedido.id

			return HttpResponseRedirect(reverse("pagamento"))

@login_required
def checkout_carrinho(request):
	form = CheckoutInfo()

	if request.session.get('carrinho'):
		anuncios = LivroAnuncio.objects.filter(id__in=[anuncio_id for anuncio_id in request.session['carrinho']])
		total = anuncios.aggregate(Sum('preco'))

	if request.method == "GET":
		return render(request, "checkout/checkout_info.html", {
			"form": form,
			"anuncios": anuncios,
			"total": total,
			"url": "checkout_carrinho"
			})

	if request.method == "POST":
		user = get_object_or_404(User, username=request.user.username)
		form = CheckoutInfo(request.POST)

		if form.is_valid():
			pedido = form.save(commit=False)
			pedido.user = user
			pedido.save()
			pedido.anuncio.add(*anuncios)
			pedido.save()

			request.session['pedido'] = pedido.id

			return HttpResponseRedirect(reverse("pagamento"))
			