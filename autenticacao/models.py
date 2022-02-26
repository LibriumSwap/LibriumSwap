from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy

class User(AbstractUser):
	email = models.EmailField(('email address'), unique=True, blank=False)
	profile_image = models.ImageField(upload_to='images/perfil/', default="images/perfil/perfil.png")
	is_funcionario = models.BooleanField(default=False)
	favoritos = models.ManyToManyField('livros.LivroAnuncio', blank=True)
