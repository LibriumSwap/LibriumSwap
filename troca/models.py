from django.db import models

from livros.models import LivroAnuncio

from django.contrib.auth import get_user_model

User = get_user_model()

class LivroTroca(models.Model):
	anuncio = models.ForeignKey(LivroAnuncio, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	titulo = models.CharField(max_length=128)
	autor = models.CharField(max_length=128)
	imagem = models.ImageField(upload_to='images/trocas')