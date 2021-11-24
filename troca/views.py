from django.shortcuts import render

from .models import LivroTroca
from .forms import LivroTrocaForm

def troca(request, anuncio_id):
	return render(request, "troca_form.html", {
		'form': LivroTrocaForm()
		})