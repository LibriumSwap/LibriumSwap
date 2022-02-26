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
	if not User.objects.filter(username=other_username):
		return redirect('chat')
	username = User.objects.get(username=request.user.username)
	otherusername = User.objects.get(username=other_username)

	if(other_username == request.user.username):
		return redirect('/chat/')
	else:
		if(Contact.objects.filter(user=username)):
			contacts_details = get_contact_details(username)
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
	threads_obj = Thread.objects.filter(thread_type="private")
	contacts_obj = Contact.objects.filter(user=username)
	contacts_list = []
	contacts_images = []
	contacts_names = []
	threads = []
	message_preview = [] 

	for contact_obj in contacts_obj:
		contacts = contact_obj


	for contact in contacts.contacts.all():
		contacts_list.append(contact)

	for contact in contacts_list:
		otherusername = contact
		contacts_names.append(contact.username)
		contacts_images.append(otherusername.profile_image.url)
		threads.append(threads_obj.filter(users__in=[username]).filter(users__in=[otherusername]))

	for thread in threads:
		message_preview.append(thread.first().message_preview)

	contacts_details = zip(contacts_names, contacts_images, message_preview)
	#print("--CONTACT--")
	#print(contacts)
	#print(contacts_names)
	#print(contacts_images)
	#print(threads)
	#print("-----------")

	return contacts_details


def get_selected_contact(username, otherusername):
	contacts_query = Contact.objects.filter(user=username, contacts__in=[otherusername])
	contact_name = ""
	for contact_query in contacts_query:
		contact_name = contact_query.contacts.first()

	contact_image = otherusername.profile_image.url
	selected_contact_details = [contact_name, contact_image]
	return selected_contact_details






