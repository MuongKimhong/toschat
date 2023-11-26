from django.db import models

from users.models import User


class ChatRoom(models.Model):
    members = models.ManyToManyField(User, related_name="members")
    created_date = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "id": self.id,
            "member_ids": [member.id for member in self.members.all()],
            "members": [member.serialize() for member in self.members.all()]
        }


class Message(models.Model):
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    text = models.TextField()
    receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "id": self.id,
            "sender": self.sender.serialize(),
            "receiver": self.receiver.serialize(),
            "chatroom_id": self.chatroom.id,
            "text": self.text
        }
