from django.shortcuts import render
from autenticacao.models import User
from django.shortcuts import render, redirect

# Create your views here.
def securityView(request):
	return render(request, "config/security.html", {})

def privacityView(request):
	return render(request, "config/privacity.html", {})

def settingsView(request):
	return render(request, "config/settings.html", {})