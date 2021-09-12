from django.urls import path

from . import views

urlpatterns = [
	path('<str:anuncio_id>/info/', views.checkout, name="checkout"),
	path('info/', views.checkout_carrinho, name="checkout_carrinho")
]