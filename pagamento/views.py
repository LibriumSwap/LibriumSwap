from django.shortcuts import render, redirect
from django.db.models import Sum

from checkout.models import Pedido
from .models import Pagamento
from .forms import PagamentoForm

def pagamento(request):
	if request.session.get("pedido"):
		form = PagamentoForm()
		pedido = Pedido.objects.get(id=request.session.get("pedido"))

		if request.method == "GET":
			return render(request, "pagamento.html", {
				"form": form,
				"anuncios": pedido.anuncio.all(),
				"total": pedido.anuncio.all().aggregate(Sum('preco'))
				})

		if request.method == "POST":
			pagamento = PagamentoForm(request.POST)

			if pagamento.is_valid():
				pagamento.save(commit=False)
				pagamento.pedido = pedido
				pagamento.save()

				return redirect("compras")
			else:
				print(pagamento.errors)
	else:
		return redirect("home")