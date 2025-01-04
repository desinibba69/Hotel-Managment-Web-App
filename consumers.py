import json
from channels.generic.websocket import AsyncWebsocketConsumer

class FAQConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        print(f"Received FAQ query: {data}")
        await self.send(text_data=json.dumps({"response": "FAQ processed"}))
