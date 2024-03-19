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
    created_time_str = models.CharField(max_length=50, blank=True)
    created_date_str = models.CharField(max_length=50, blank=True)

    def serialize(self):
        return {
            "sender": self.sender.serialize(),
            "message": {"id": self.id, "text": self.text},
            "chatroom_id": self.chatroom.id,
            "time": self.created_time_str,
            "type": "message"
        }

    def update_blank_field(self) -> None:
        if not self.created_date_str.strip():
            self.created_date_str = self.created_date.date().strftime('%d/%m/%Y')

        if not self.created_time_str.strip():
            self.created_time_str = self.created_date.strftime("%I:%M %p")

        self.save()