from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.slug


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.content} - {self.room}"

    class Meta:
        ordering = ('created_at',)
