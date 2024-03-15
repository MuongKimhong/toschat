from typing import Dict, Union

from django.db import models

from account.models import User, UserContact


class ChatRoom(models.Model):
    members = models.ManyToManyField(User)
    created_date = models.DateTimeField(auto_now_ad=True)

    def serialize(self) -> Dict[str, Union[str, list[Dict[str, str]]]]:
        return {
            "id": str(self.id),
            "members": [member.serialize() for member in self.members.all()]
        }


class Message(models.Model):
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_ad=True)

    def serialize(self):
        return {
            "sender": self.sender.serialize(),
            "message": {"id": str(self.id), "text": self.text}
        }
