from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from django.shortcuts import render, redirect
from .models import Contact
from autenticacao.models import User
import json

# Create your views here.
@login_required
def chatView(request):
	username = User.objects.get(username=request.user.username)
	if(Contact.objects.filter(user=username)):
			querys = Contact.objects.filter(user=username)
			return render(request, 'chat/chat.html', {
				'username': mark_safe(json.dumps(request.user.username)),
				'querys': querys,
				})
	else:
		return render(request, 'chat/chat.html', {
			'username': mark_safe(json.dumps(request.user.username)),
			})

@login_required
def roomView(request, other_username):
	username = User.objects.get(username=request.user.username)
	if(other_username == request.user.username):
		return redirect('/chat/')
	else:
		if(Contact.objects.filter(user=username)):
			querys = Contact.objects.filter(user=username)

			return render(request, 'chat/room.html', {
				'username': mark_safe(json.dumps(request.user.username)),
				'other_username': other_username,
				'querys': querys,
				})
		else:
			return render(request, 'chat/room.html', {
				'username': mark_safe(json.dumps(request.user.username)),
				'other_username': other_username,
				})
