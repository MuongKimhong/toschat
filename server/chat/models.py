from django.db import models


class ChatRoom(models.Model):
    members = models.ManyToManyField("account.User")
    created_date = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "id": self.id,
            "members": [member.serialize() for member in self.members.all()]
        }


class Message(models.Model):
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey("account.User", on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "sender": self.sender.serialize(),
            "message": {"id": self.id, "text": self.text},
            "chatroom_id": self.chatroom.id,
            "time": self.created_date.strftime("%I:%M %p"),
            "type": "message"
        }
