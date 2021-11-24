from django.db import models

class LivroTroca(models.Model):
	titulo = models.CharField(max_length=128)
	autor = models.CharField(max_length=128)
	imagem = models.ImageField(upload_to='images/trocas')