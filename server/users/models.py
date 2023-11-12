from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.id}"
    
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "created_date": date_format(self.created_date),
        }
