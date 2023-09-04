from channels.generic.websocket import AsyncWebsocketConsumer
from django.db.models import Q
from channels.db import database_sync_to_async
from socials.models import *
from authentication.models import *
import json


class ChatRoomConsumer(AsyncWebsocketConsumer):
   
    async def connect(self):
        receiver_id = self.scope['url_route']['kwargs']['pk']
        print(receiver_id)
        print(self.scope['user'].pk)
        sender_id = self.scope['user']
        self.room_name = self.scope['user'].pk
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        user = await self.get_user_object(receiver_id)
        chat = await self.get_chat_messages(sender_id, receiver_id)

        await self.accept()
        await self.send(json.dumps(chat))



    async def receive(self, text_data):
         print(self.scope)
         receiver_id = self.scope['url_route']['kwargs']['pk']
         sender_id = self.scope['user']
         data = json.loads(text_data)
         message= data['message']
         chat = await self.create_chat_messages(sender_id, receiver_id,message)
         
         
         await self.channel_layer.group_send(
             self.room_group_name,
             {
                 'type': 'chat_message',
                 'message': chat,
                 'receiver_id': receiver_id,
                 'sender_id': sender_id.id
             }

         )
         
    async def chat_message(self, event):
        message = event['message']
        receiver_id = event['receiver_id']
        sender_id = event['sender_id']
         
        data = {
            'message': message,
            'receiver_id': int(receiver_id),
            'sender_id': sender_id,
        }
        text_data = json.dumps(data)
        await self.send(text_data)

    @database_sync_to_async
    def create_chat_messages(self, sender_id, receiver_id,message):
        receiver =  MyUser.objects.get(id=receiver_id)
        try:
            chat = Chat.objects.get(owner=sender_id, receiver=receiver_id)
        except:
            chat = Chat.objects.create(owner=sender_id, receiver=receiver_id)
        
        messages = Message.objects.create(chat=chat, owner=sender_id, receiver=receiver, body= message)
        main_chat = chat.message.all()
        messages = []
        for msg in  main_chat:
            messages.append({
                'receiver': msg.receiver.id,
                'owner': msg.owner.id,
                'body': msg.body 
            })
        return messages
        

    

    @database_sync_to_async
    def get_user_object(self, receiver_id):
        receiver = MyUser.objects.get(id=receiver_id)
        return receiver
    
    @database_sync_to_async  
    def get_chat_messages(self, sender_id, receiver_id):
        try:
            chat = Chat.objects.get(Q(owner=sender_id, receiver=receiver_id)|Q(owner=receiver_id, receiver=sender_id))
        except:
            chat = Chat.objects.create(owner=sender_id, receiver=receiver_id)
        response = {
            'owner': chat.owner.username,
            #'timestamp': chat.timestamp.time,
            'receiver': chat.receiver.username
        }
        return response



    

  



#sudo service redis-server restart



