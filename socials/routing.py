from django.urls import path
from .consumers import MyConsumer

ws_urlpatterns = [
    path('ws/posts/', MyConsumer.as_asgi())
]