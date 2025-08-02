import json
from channels.generic.websocket import AsyncWebsocketConsumer

class InspectorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.session_id = self.scope['url_route']['kwargs']['session_id']
        await self.channel_layer.group_add(self.session_id, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.session_id, self.channel_name)

    async def new_request(self, event):
        await self.send(text_data=json.dumps(event['data']))