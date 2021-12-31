import mercadopago

from django.shortcuts import render, redirect
from django.db.models import Sum
from django.conf import settings

from checkout.models import Pedido
from .models import Pagamento

from django.contrib.auth import get_user_model

User = get_user_model()

def pagamento(request):
	if request.session.get("pedido"):
		pedido = Pedido.objects.get(id=request.session.get("pedido"))
		total = pedido.anuncio.all().aggregate(Sum('preco'))
		user = User.objects.get(username=request.user.username)

		# Adicione as credenciais
		sdk = mercadopago.SDK(settings.MERCADO_PAGO_ACCESS_TOKEN)
		# Cria um item na preferência
		preference_data = {
			"items": [
				{
					"title": pedido.anuncio.first().titulo,
					"quantity": 1,
					"unit_price": total.get('preco__sum')
				}
			],
			"payer": {
				"name": user.username,
				"email": user.email,
				
				"identification": {
					"type": "CPF",
					"number": pedido.cpf
				},
				"address": {
					"street_name": pedido.rua,
					"street_number": pedido.numero,
					"zip_code": pedido.cpf
				}
			},
			"back_urls": {
				"success": "http://127.0.0.1:8000/payment/success",
				"failure": "http://www.failure.com",
				"pending": "http://www.pending.com"
			},
			"auto_return": "approved",
		}

		preference_response = sdk.preference().create(preference_data)
		preference = preference_response["response"]

		return render(request, 'pagamento.html', {
			'preference_id': preference['id'],
			'anuncios': pedido.anuncio.all(),
			'total': total
			})
	else:
		return redirect("home")

def pagamento_success(request):
	pedido = Pedido.objects.get(id=request.session.get("pedido"))

	if pedido.pago == True:
		return redirect('home')
	else:
		total = pedido.anuncio.all().aggregate(Sum('preco'))
		pagamento = Pagamento(pedido=pedido, total=total.get('preco__sum'))
		pagamento.save()
		pagamento.pedido.pago = True
		pagamento.pedido.save()
		pagamento.save()

	return redirect("compras")