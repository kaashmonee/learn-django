# chat/routing.py
from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    # Some regex that I don't really know what it does ATM
    # Looks like it tells people to go to the consumers.ChatConsumer class
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
]