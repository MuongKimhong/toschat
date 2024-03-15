from django.contrib.auth.hashers import make_password
from account.models import User


def create_dummy_users(count: int):
    for i in range(count):
        User.objects.create(
            username=f"Username{i+1}",
            password=make_password("123456789")
        )