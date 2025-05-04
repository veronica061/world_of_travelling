import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ReviewsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "reviews"
        self.room_group_name = f"reviews_{self.room_name}"

        # Присоединяемся к группе
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Отсоединяемся от группы
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def new_review(self, event):
        text = event['text']
        author = event['author']
        created_at = event['created_at']

        # Отправляем сообщение WebSocket клиенту
        await self.send(text_data=json.dumps({
            'text': text,
            'author': author,
            'created_at': created_at
        }))
