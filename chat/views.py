from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from django.shortcuts import render
import json

# Create your views here.
@login_required
def chatView(request):
	return render(request, 'chat/chat.html', {'username': mark_safe(json.dumps(request.user.username))})

@login_required
def roomView(request, other_username):
	return render(request, 'chat/room.html', {
		'username': mark_safe(json.dumps(request.user.username)),
		'other_username': other_username
		})