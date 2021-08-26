from django.urls import path

from . import views

urlpatterns = [
	path('<str:anuncio_id>/info/', views.checkout_info, name="checkout_info")
]