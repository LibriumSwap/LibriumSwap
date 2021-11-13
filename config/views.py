from django.shortcuts import render
from autenticacao.models import User
from django.shortcuts import render, redirect
from .forms import ConfigForm

# Create your views here.
def securityView(request):
	return render(request, "config/security.html", {})

def privacityView(request):
	return render(request, "config/privacity.html", {})

def settingsView(request):
	username = User.objects.get(username=request.user.username)
	if request.method == "POST":
		form = ConfigForm(request.FILES)
		if form.is_valid():
			image = form.cleaned_data['profile_image']
			username.profile_image = image
			username.save()
			return redirect('settings')
		else:
			return render(request, "config/settings.html", {
				"form": form,
				})
	else:
		return render(request, "config/settings.html", {
			"form": ConfigForm(),
			})