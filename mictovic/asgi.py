"""
ASGI config for mictovic project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from django.conf import settings
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from socials.routing import ws_urlpatterns



# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mictovic.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
 'http': django_asgi_app,
 'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns))
})
