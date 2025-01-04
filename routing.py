from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/faq/', consumers.FAQConsumer.as_asgi()),  # WebSocket route for the FAQ section
]
