from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from django.urls import reverse

from .forms import LoginForm, RegisterForm
from .models import CustomUser as User

def login_view(request):
	if request.method == 'POST':
		username = request.POST["username"]
		password = request.POST["password"]

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse("index"))
		else:
			return render(request, "autenticacao/login.html", {
				"form": LoginForm(),
				"message": "Usuário e/ou senha inválidos."
			})
	else:
		return render(request, "autenticacao/login.html", {
			"form": LoginForm()
			})

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse("index"))

def register(request):
	if request.method == "POST":
		username = request.POST["username"]
		email = request.POST["email"]

		# Checar se as senhas são iguais
		password1 = request.POST["password1"]
		password2 = request.POST["password2"]
		if password1 != password2:
			return render(request, "autenticacao/register.html", {
				"form": RegisterForm(),
				"message": "As senhas não correspondem."
			})

		# Tentar criar novo usuário
		try:
			user = User.objects.create_user(username, email, password1)
			user.save()

		except IntegrityError:
			return render(request, "autenticacao/register.html", {
				"form": RegisterForm(),
				"message": "Nome de usuário já está em uso."
			})
		login(request, user)
		return HttpResponseRedirect(reverse("index"))
	else:
		return render(request, "autenticacao/register.html", {
			"form": RegisterForm()
			})