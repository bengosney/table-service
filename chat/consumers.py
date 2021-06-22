# Standard Library
import json
from math import floor
from random import random

# Third Party
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        self.id = floor(random() * 8999) + 1000

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": f"{self.id} has joined the room"}
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": f"{self.id} has left the room"}
        )
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        await self.channel_layer.group_send(self.room_group_name, {"type": "chat_message", "message": message})

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
