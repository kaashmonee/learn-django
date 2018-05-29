# chat/consumers.py
from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer


# This is just the "consumer" class, which means they are the ones who are doing
# the communicating through the socket
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Obtains the room name parameter from the URL in chat/routes.py, which
        # WAs responsible for opening the websocket
        # Every ChatConsumer has a self.scope variable -- contains information
        # about connection, including particular any positional or kwargs
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        # Creates a Channels group name directly from user-specified room name,
        # without quoting or escaping --- only contain digits, hyphens, and 
        # periods
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        # Responsible for joining a group
        # Async to sync is necessary because ChatConsumer is a synchronous 
        # websocket but it scalling an asynchronous channel layer method
            # This is interesting, because I'm not sure where the synchronous
            # stuff is happening
        # Group names -- restricted to ASCII alphanumerics, hyphens, periods
        # code constructs a group name directly from room name, fails if room
        # name contains characters that aren't valid in group name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receieve a message from the websocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # send message to room group
        print("group_send type:", type(self.channel_layer.group_send))
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to websocket
        await self.send(text_data=json.dumps({
            "message": message
        }))