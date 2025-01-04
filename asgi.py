"""
ASGI config for HotelManagementSystem project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import hotel.routing  # Import your app's routing module

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HotelManagementSystem.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Handle traditional HTTP requests
    "websocket": AuthMiddlewareStack(
        URLRouter(
            hotel.routing.websocket_urlpatterns  # Define WebSocket URL routes here
        )
    ),
})
