from django.contrib import admin
from chat.models import Message, Thread

admin.site.register(Thread)
admin.site.register(Message)