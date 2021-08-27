from django.shortcuts import render

def carrinho(request):
	return render(request, "carrinho.html", {})