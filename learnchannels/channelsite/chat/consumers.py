# chat/consumers.py
from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
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
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receieve a message from the websocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]

        # Send message to websocket
        self.send(text_data=json.dumps({
            "message": message
        }))