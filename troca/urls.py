from django.urls import path

from . import views

urlpatterns = [
	path('new/<str:anuncio_id>', views.troca, name="troca"),
]