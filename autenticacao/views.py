from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.db import IntegrityError
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError
from django.contrib.sites.shortcuts import get_current_site


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

def password_reset_request(request):
	if request.method == "POST":
		form = PasswordResetForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data['email']
			user = User.objects.get(Q(email=data))
			current_site = get_current_site(request)
			if user:
				subject = "Solicitação de troca de senha"
				email_template_name = "registration/password_reset_email.txt"
				c = {
				"email":user.email,
				'domain': current_site.domain,
				'site_name': current_site.name,
				"uid": urlsafe_base64_encode(force_bytes(user.pk)),
				"user": user,
				'token': default_token_generator.make_token(user),
				'protocol': 'http',
				}
				email = render_to_string(email_template_name, c)
				try:
					send_mail(subject, email, 'admin@libriumswap.live' , [user.email], fail_silently=False)
				except BadHeaderError:
					return HttpResponse('Invalid header found.')
				return redirect ("/reset-password/done")
			return HttpResponseRedirect(reverse('index'))
	return render(request, template_name="registration/password_reset_form.html", context={"form":PasswordResetForm()})