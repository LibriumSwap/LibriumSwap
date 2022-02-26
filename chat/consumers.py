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
        user = self.scope['user']
        username = User.objects.get(username=user)
        other_username = self.scope['url_route']['kwargs']['other_username']
        other_user = User.objects.get(username=other_username)
        thread_type = Thread.objects.filter(thread_type='private') # filter all threads
        thread_obj = self.get_or_create_private_thread(username, other_user) # get or create a thread
        self.room_group_name = f'private_thread_{thread_obj.id}'
        print(self.room_group_name)
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
        self.new_contact(username, other_user) # create contact

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
        self.send(text_data=json.dumps(message))

    def chat_message(self, data):
        message = data['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps(message))

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def fetch_messages(self, data):
        user = self.scope['user']
        other_username = self.scope['url_route']['kwargs']['other_username']
        other_user = User.objects.get(username=other_username)

        threads = self.get_current_thread(user, other_user)
        thread_obj = threads.get(thread_type="private")
        thread_id = thread_obj.id  
        message = Message.objects.filter(thread_id=thread_id) #get messages from a specific thread
        messages = self.last_10_messages(message) # fetch messages
        content = {
            'command': 'messages',
            'messages': self.messages_to_jsn(messages),
        }

        self.send_message(content)

    def new_message(self, data):
        author = data['from']
        author_user = User.objects.filter(username=author)[0]

        user = self.scope['user']
        other_username = self.scope['url_route']['kwargs']['other_username']
        other_user = User.objects.get(username=other_username)

        threads = self.get_current_thread(user, other_user) # filter threads
        thread_obj = threads.get(thread_type="private") # get thread specific object

        contact_obj = Contact.objects.get(user=user)

        message = Message.objects.create(author=author_user, contact=contact_obj, content=data['message'], thread=thread_obj)
        content = {
            'author': author,
            'command': 'new_message',
            'message': self.message_to_jsn(message)
        }

        #get preview message
        thread_obj = threads.get(thread_type="private")
        thread_id = thread_obj.id 
        self.save_preview_message(user, other_user, thread_id) 

        return self.send_chat_message(content)


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

    def get_current_thread(self, user1, user2):
        threads = Thread.objects.filter(thread_type='private')
        threads = threads.filter(users__in=[user1]).filter(users__in=[user2])
        return threads

    def last_10_messages(self, messages):
        all_messages = messages.order_by('-timestamp').all()[:10]

        reverse_message_list = list(reversed(all_messages))

        return reverse_message_list

    def save_preview_message(self, username, other_user, thread_id):
        messages = Message.objects.filter(thread_id=thread_id)
        if messages.exists():
            message = messages.order_by('-timestamp').reverse().last()
            content = message.content

            thread = self.get_current_thread(username, other_user)
            thread_obj = thread.get(thread_type='private')
            thread_obj.message_preview = content
            thread_obj.save()
    
    #Create contact
    def new_contact(self, username, other_username):
        #Object
        otherusername_obj = User.objects.get(username=other_username)
        username_obj = User.objects.get(username=username)

        #print("--NEW CONTACT--")
        if Contact.objects.filter(user=username_obj):
            #print("ADDED CONTACT")
            otheruser_image = otherusername_obj.profile_image
            contact_obj = Contact.objects.get(user=username_obj)
            contact_obj.contacts.add(otherusername_obj)
            #print("-------------")
        else:
            #print("CREATED CONTACT AND ADDED")
            otheruser_image = otherusername_obj.profile_image
            contact_obj = Contact.objects.create(user=username)
            contact_obj.contacts.add(otherusername_obj)
            content = {
                'command': 'new_contact',
                'contact': self.contact_to_json(contact_obj, otheruser_image)
            }
            #print("--------------")
            self.send(text_data=json.dumps(content))

    def contact_to_json(self, contact, otheruser_image):
        return {
            'contact_name': contact.contacts.first().username,
            'contact_image': otheruser_image.url,
        }

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message,
    }