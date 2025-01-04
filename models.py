# hotel/models.py

from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()

    def __str__(self):
        return self.name

class Room(models.Model):
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.room_type} - {self.room_number}"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    check_in_date = models.DateField()
    check_out_date = models.DateField(null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
