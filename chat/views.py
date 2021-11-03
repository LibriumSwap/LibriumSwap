from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from django.shortcuts import render, redirect
from .models import Contact, Thread
from autenticacao.models import User
import json

# Create your views here.
@login_required
def chatView(request):
	username = User.objects.get(username=request.user.username)
	if(Contact.objects.filter(user=username)):
		contacts_query = Contact.objects.filter(user=username)
		#threads_query = Thread.objects.filter(thread_type="private")
		#threads = threads_query.filter(users__in=[username]).filter(users__in=[otherusername])

		return render(request, 'chat/chat.html', {
			'username': mark_safe(json.dumps(request.user.username)),
			'contacts_query': contacts_query,

			})
	else:
		return render(request, 'chat/chat.html', {
			'username': mark_safe(json.dumps(request.user.username)),
			})

@login_required
def roomView(request, other_username):
	username = User.objects.get(username=request.user.username)
	otherusername = User.objects.get(username=other_username)
	if(other_username == request.user.username):
		return redirect('/chat/')
	else:
		if(Contact.objects.filter(user=username)):
			contacts_query = Contact.objects.filter(user=username)
			threads_query = Thread.objects.filter(thread_type="private")
			threads = threads_query.filter(users__in=[username]).filter(users__in=[otherusername])
			contact_name_query = Contact.objects.filter(user=username, contacts__in=[otherusername])

			return render(request, 'chat/room.html', {
				'username': mark_safe(json.dumps(request.user.username)),
				'other_username': other_username,
				'contacts_query': contacts_query,
				'threads': threads,
				'contact_name_query': contact_name_query,
				})
		else:
			return render(request, 'chat/room.html', {
				'username': mark_safe(json.dumps(request.user.username)),
				'other_username': other_username,
				})


