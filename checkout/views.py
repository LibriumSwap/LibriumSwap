from django.shortcuts import render

from livros.models import LivroAnuncio
from .forms import CheckoutInfo

def checkout_info(request, anuncio_id):
	form = CheckoutInfo()
	anuncio = LivroAnuncio.objects.get(id=anuncio_id)

	return render(request, "checkout/checkout_info.html", {
		"form": form,
		"anuncio": anuncio
		})