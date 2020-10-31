import uuid

from django.db import models
from django.utils import timezone


class Room(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    room = models.ForeignKey(
        Room,
        blank=True,
        null=True,
        related_name='room_meesages',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
