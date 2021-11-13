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
				pagamento_object = pagamento.save()

				pagamento_object.pedido = pedido
				total = pagamento_object.pedido.anuncio.aggregate(Sum('preco'))
				pagamento_object.total = total.get('preco__sum')
				pagamento_object.pedido.pago = True
				pagamento_object.pedido.save()
				pagamento_object.save()

				return redirect("compras")
			else:
				print(pagamento.errors)
	else:
		return redirect("home")