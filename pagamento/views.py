from django.shortcuts import render
from LibriumSwap.settings import MERCADO_PAGO_ACCESS_TOKEN, MERCADO_PAGO_ACCESS_TOKEN
import mercadopago

sdk = mercadopago.SDK(MERCADO_PAGO_ACCESS_TOKEN)

def pagamento(request):

	payment_data = {
	    "transaction_amount": float(52),
	    "token": MERCADO_PAGO_ACCESS_TOKEN,
	    "description": "foda",
	    "installments": int(1),
	    "payment_method_id": "visa",
	    "payer": {
	        "email": "ricardo.csantos0877@gmail.com",
	        "identification": {
	            "type": "CPF", 
	            "number": 19119119100
	        }
	    }
	}

	payment_response = sdk.payment().create(payment_data)
	payment = payment_response["response"]

	print(payment)