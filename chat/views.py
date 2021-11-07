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
		contacts_details = get_contact_details(username)

		return render(request, 'chat/chat.html', {
			'username': mark_safe(json.dumps(request.user.username)),
			'contacts_details': contacts_details,
			})
	else:
		return render(request, 'chat/chat.html', {
			'username': mark_safe(json.dumps(request.user.username)),
			})

@login_required
def roomView(request, other_username):
	username = User.objects.get(username=request.user.username)
	otherusername = User.objects.get(username=other_username)
	contacts_details = get_contact_details(username)
	if(other_username == request.user.username):
		return redirect('/chat/')
	else:
		if(Contact.objects.filter(user=username)):
			selected_contact_details = get_selected_contact(username, otherusername)
			return render(request, 'chat/room.html', {
				'username': mark_safe(json.dumps(request.user.username)),
				'other_username': other_username,
				'contacts_details': contacts_details,
				'selected_contact_details': selected_contact_details,
				})
		else:
			return render(request, 'chat/room.html', {
				'username': mark_safe(json.dumps(request.user.username)),
				'other_username': other_username,
				})




def get_contact_details(username):
	threads_query = Thread.objects.filter(thread_type="private")
	contacts_query = Contact.objects.filter(user=username)
	contacts = []
	for contact_query in contacts_query:
		contacts.append(contact_query)

	contacts_images = []
	contacts_names = []
	threads = []
	for contact in contacts:
		otherusername = User.objects.get(username=contact.contacts.first())
		contacts_names.append(contact.contacts.first())
		contacts_images.append(otherusername.profile_image.url)
		threads.append(threads_query.filter(users__in=[username]).filter(users__in=[otherusername]))

	message_preview = [] 
	for thread in threads:
		message_preview.append(thread.first().message_preview)

	contacts_details = zip(contacts_names, contacts_images, message_preview)

	return contacts_details


def get_selected_contact(username, otherusername):
	contacts_query = Contact.objects.filter(user=username, contacts__in=[otherusername])
	contact_name = ""
	for contact_query in contacts_query:
		contact_name = contact_query.contacts.first()

	contact_image = otherusername.profile_image.url
	selected_contact_details = [contact_name, contact_image]
	return selected_contact_details






