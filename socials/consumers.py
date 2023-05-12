from channels.generic.websocket import AsyncWebsocketConsumer
from django.http import JsonResponse
import json


class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'mygroup',
            self.channel_name,
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            'mygroup',
            self.channel_name,
        )

    async def recieve(self, text_data):
        pass

    async def send_post(self, event):
        #data2 = event['text']
        data = json.loads(event['text'])
        await self.send(text_data= json.dumps(data))


#sudo service redis-server restart
