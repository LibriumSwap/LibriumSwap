from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Sum

from livros.models import LivroAnuncio
from .forms import CheckoutInfo

@login_required
def checkout(request, anuncio_id):
	form = CheckoutInfo()
	anuncios = []
	anuncio = get_object_or_404(LivroAnuncio, id=anuncio_id)
	total = {'preco__sum': anuncio.preco}

	anuncios.append(anuncio)

	return render(request, "checkout/checkout_info.html", {
		"form": form,
		"anuncios": anuncios,
		"total": total
		})

@login_required
def checkout_carrinho(request):
	form = CheckoutInfo()

	if request.session.get('carrinho'):
		anuncios = LivroAnuncio.objects.filter(id__in=[anuncio_id for anuncio_id in request.session['carrinho']])
		total = anuncios.aggregate(Sum('preco'))

	return render(request, "checkout/checkout_info.html", {
		"form": form,
		"anuncios": anuncios,
		"total": total
		})