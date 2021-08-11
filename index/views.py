from django.shortcuts import render
from django.http import HttpResponseRedirect
from livros.models import LivroAnuncio


def index(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect("home")
	else:
		return render(request, "index/index.html")

def home(request):
	recentes = LivroAnuncio.objects.all().order_by('id')[:11]
	return render(request, "home/home.html", {
		"recentes": recentes
		})