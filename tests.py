from django.test import TestCase

from django.test import TestCase
from .models import Room

class RoomModelTest(TestCase):
    def setUp(self):
        Room.objects.create(room_number="101", room_type="Deluxe", is_available=True, price_per_night=200)

    def test_room_creation(self):
        room = Room.objects.get(room_number="101")
        self.assertEqual(room.room_type, "Deluxe")
        self.assertEqual(room.price_per_night, 200)
