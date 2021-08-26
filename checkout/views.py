from django.shortcuts import render

from livros.models import LivroAnuncio

def checkout_info(request, anuncio_id):
	return render(request, "checkout/checkout_info.html")