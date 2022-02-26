from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Contact(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    contacts = models.ManyToManyField('autenticacao.User')

    def __str__(self):
        return f'{self.user.username}'

class Thread(models.Model):
    THREAD_TYPE = (
        ('private', 'Private'),
        ('group', 'Group')
        )
    name = models.CharField(max_length=50, null=True, blank=True)
    thread_type = models.CharField(max_length=15, choices=THREAD_TYPE, default='private')
    message_preview = models.TextField(blank=True)
    users = models.ManyToManyField('autenticacao.User')


    def __str__(self) -> str:
        if self.thread_type == 'private' and self.users.count() == 2:
            return f'{self.users.first()} and {self.users.last()}'
        return f'{self.name}'

class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, related_name='contact_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    thread = models.ForeignKey(Thread, related_name="thread_messages", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.thread.users.first().username} to {self.thread.users.last().username}: {self.content}'


