from typing import Dict

from django.contrib.auth.models import AbstractUser
from django.db import models

from chat.models import ChatRoom


class User(AbstractUser):
    username = models.CharField(max_length=200, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.username} - {self.id}"

    def serialize(self) -> Dict[str, str]:
        return {"id": self.id, "username": self.username}


class UserContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.ForeignKey(User, related_name="contact", on_delete=models.CASCADE)
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def serialize(self) -> Dict[str, Dict[str, str]]:
        data = {
            "user": self.user.serialize(),
            "contact": self.contact.serialize()
        }
        data["contact"]["chatroom_id"] = self.chatroom.id
        return data
