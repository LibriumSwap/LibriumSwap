from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
	email = models.EmailField(_('email address'), unique=True, blank=False)
	enderecos = models.ManyToManyField('EnderecoUser')
	is_funcionario = models.BooleanField(default=False)

class EnderecoUser(models.Model):
	nome_user = models.CharField(max_length=128)
	cpf = models.CharField(max_length=11)
	contato = models.CharField(max_length=11)
	cep = models.CharField(max_length=8)
	estado = models.CharField(max_length=64)
	cidade = models.CharField(max_length=64)
	rua = models.CharField(max_length=128)
	complemento = models.CharField(max_length=128)
	numero = models.CharField(max_length=10)