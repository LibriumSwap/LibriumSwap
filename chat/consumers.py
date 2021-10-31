# chat/consumers.py
from django.contrib.auth import get_user_model
import json
from django.db.models import Count
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Thread, Message, Contact

User = get_user_model()
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        username = self.scope['user']
        other_username = self.scope['url_route']['kwargs']['other_username']
        other_user = User.objects.get(username=other_username)
        self.create_contact(username, other_user)
        thread_type = Thread.objects.filter(thread_type='private')
        thread_obj = self.get_or_create_private_thread(username, other_user)
        self.room_group_name = f'private_thread_{thread_obj.id}'

        print(self.room_group_name)
        #self.room_group_name = f'private_thread_'
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def send_chat_message(self, message):
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def send_message(self, message):
        create_contact(username=self.scope['user'], other_username=self.scope['url_route']['kwargs']['other_username'])
        self.send(text_data=json.dumps(message))

    def create_contact(self, username, other_username):
        user = User.objects.get(username=username)
        contact_name = User.objects.get(username=other_username)
        contacts = Contact.objects.all()
        if(user == contact_name):
            print("1")
        else:
            user_name = User.objects.filter(username=username)
            otheruser_name = User.objects.filter(username=other_username)
            if(contacts.filter(user__in=user_name, contacts__in=otheruser_name).exists()):
                print("2")
            else:
                print("3")
                contact = Contact.objects.create(user=user)
                contact.contacts.add(contact_name)

    def chat_message(self, data):
        message = data['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps(message))

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def get_or_create_private_thread(self, user1, user2):
        threads = Thread.objects.filter(thread_type='private')

        threads = threads.filter(users__in=[user1, user2]).distinct()

        threads = threads.annotate(u_count=Count('users')).filter(u_count=2)
        if threads.exists():
            return threads.first()
        else:
            thread = Thread.objects.create(thread_type='private')
            thread.users.add(user1)
            thread.users.add(user2)
            return thread

    def fetch_messages(self, data):
        messages = Message.last_20_messages()
        content = {
            'command': messages,
            'messages': self.messages_to_jsn(messages),
        }

        self.send_message(content)

    def new_message(self, data):
        author = data['from']
        author_user = User.objects.filter(username=author)[0]
        message = Message.objects.create(author=author_user, content=data['message'])
        content = {
            'author': author,
            'command': 'new_message',
            'message': self.message_to_jsn(message)
        }
        return self.send_chat_message(content)

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message
    }

    def messages_to_jsn(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_jsn(message))
        return result

    def message_to_jsn(self, message):
        return {
            'author': message.author.username,
            'content': message.content,
            'timestamp': str(message.timestamp)
        }