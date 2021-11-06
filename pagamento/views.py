from django.shortcuts import render
from LibriumSwap.settings import MERCADO_PAGO_ACCESS_TOKEN, MERCADO_PAGO_ACCESS_TOKEN
import mercadopago

sdk = mercadopago.SDK(MERCADO_PAGO_ACCESS_TOKEN)

def pagamento(request):
	if request.method == "GET":
		return render(request, "pagamento.html")

	if request.method == "POST":
		pass