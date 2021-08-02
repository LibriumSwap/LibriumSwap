from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

def login_view(request):
	if request.method == 'POST':
		username = request.POST["username"]
		password = request.POST["password"]

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse("index"))
		else:
			return render(request, "books/login.html", {
			"message": "Usuário e/ou senha inválidos."
			})
	else:
		return render(request, "books/login.html")

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse("index"))

def register(request):
	if request.method == "POST":
		username = request.POST["username"]
		email = request.POST["email"]

		# Checar se as senhas são iguais
		password = request.POST["password"]
		password_confirm = request.POST["password_confirm"]
		if senha != senha_confirmacao:
			return render(request, "books/register.html", {
			"message": "As senhas não correspondem."
			})

		# Tentar criar novo usuário
		try:
			user = User.objects.create_user(username, email, password)
			user.save()

		except IntegrityError:
			return render(request, "books/register.html", {
			"message": "Nome de usuário já está em uso."
			})
		login(request, user)
		return HttpResponseRedirect(reverse("index"))
	else:
		return render(request, "books/register.html")