from django.urls import path

from . import views

urlpatterns = [
	path('', views.pagamento, name="pagamento"),
	path('success', views.pagamento_success, name="payment_success")
]