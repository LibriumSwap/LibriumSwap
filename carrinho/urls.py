from django.urls import path

from . import views

urlpatterns = [
	path("", views.carrinho, name="carrinho"),
	path("adicionar/", views.adicionar_ao_carrinho, name="adicionar_ao_carrinho")
]