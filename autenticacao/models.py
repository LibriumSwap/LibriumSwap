from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy

class User(AbstractUser):
	favoritos = models.ManyToManyField('livros.LivroAnuncio')
	email = models.EmailField(('email address'), unique=True, blank=False)
	pedidos = models.ManyToManyField('checkout.Pedido')
	is_funcionario = models.BooleanField(default=False)