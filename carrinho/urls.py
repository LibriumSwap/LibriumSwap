from django.urls import path

from . import views

urlpatterns = [
	path("", views.carrinho, name="carrinho"),
	path("adicionar/", views.adicionar_ao_carrinho, name="adicionar_ao_carrinho"),
	path("remover/", views.remover_do_carrinho, name="remover_do_carrinho")
]