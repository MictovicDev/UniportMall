from django.urls import re_path
from .consumers import ChatRoomConsumer

ws_urlpatterns = [
    # path('chat/', ChatRoomConsumer.as_asgi())
    re_path(r'ws/chat/(?P<pk>\w+)/$', ChatRoomConsumer.as_asgi())
]
