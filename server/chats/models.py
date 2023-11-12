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
