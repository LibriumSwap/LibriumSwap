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
			if len(request.FILES) > 0:
				username.profile_image = request.FILES['profile_image']
				username.save()
				return redirect('profile')

		elif address_form.is_valid():
			print("valido")
			return redirect('chat')

		else:
			return render(request, "config/settings/profile.html", {
				"config_form": config_form,
				"address_form": address_form,
				"username": username,
				})

		

	return render(request, "config/settings/profile.html", {
		"config_form": ConfigForm(),
		"address_form": CheckoutInfo(),
		"username": username,
	})

def paymentView(request):
	return render(request, "config/settings/payment.html", {})

def newPaymentView(request):
	return render(request, "config/settings/new-payment.html", {})


def notificationsView(request):
	return render(request, "config/settings/notifications.html", {})