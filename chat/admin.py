from django.contrib import admin
from chat.models import Message, Thread, Contact

admin.site.register(Thread)
admin.site.register(Message)
admin.site.register(Contact)