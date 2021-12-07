from django.urls import path

from . import views

urlpatterns = [
	path('new/<str:anuncio_id>', views.troca, name="troca"),
	path('solicitations', views.trocas_solicitadas, name="trocas_solicitadas"),
	path('received', views.trocas_recebidas, name="trocas_recebidas"),
	path('accept', views.aceitar_troca, name="aceitar_troca"),
	path('refuse', views.recusar_troca, name="recusar_troca")
]