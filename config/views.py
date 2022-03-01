from django.shortcuts import render
from autenticacao.models import User
from django.shortcuts import render, redirect
from .forms import ConfigForm
from checkout.forms import CheckoutInfo

# Create your views here.
def securityView(request):
	return render(request, "config/security.html", {})

def privacityView(request):
	return render(request, "config/privacity.html", {})

def settingsView(request):
	return render(request, "config/settings.html", {})

def profileView(request):
	username = User.objects.get(username=request.user.username)
	if request.method == "POST":
		config_form = ConfigForm(request.POST, request.FILES)
		address_form = CheckoutInfo(request.POST, instance=username)
		if config_form.is_valid():
			print("1")
			if 'profile_image' in request.POST:
				print(request.POST['profile_image'])
				if request.POST['profile_image'] != "media/images/perfil/":
					print("1")
					image = "images/perfil/" + request.POST['profile_image']
					username.profile_image = image
					username.save()
					return redirect('profile')
				else:
					print("2")
			else:
				print("2")
				return render(request, "config/settings/profile.html", {
				"config_form": config_form,
				"address_form": address_form,
				"username": username,
				})
		else:
			print("2")
			return render(request, "config/settings/profile.html", {
				"config_form": config_form,
				"address_form": address_form,
				"username": username,
				})
	else:
		return render(request, "config/settings/profile.html", {
			"config_form": ConfigForm(),
			"address_form": CheckoutInfo(),
			"username": username,
			})

def paymentView(request):
	return render(request, "config/settings/payment.html", {})

def notificationsView(request):
	return render(request, "config/settings/notifications.html", {})