from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.cache import cache
from account.models import User
import time


def create_dummy_users(count: int):
    for i in range(count):
        User.objects.create(
            username=f"Username{i+1}",
            password=make_password("123456789")
        )


def get_access_token_time(user):
    start = time.time()
    refresh_token = RefreshToken.for_user(user) 
    access_token  = refresh_token.access_token
    data = {
        'user': user.serialize(),
        'access_token' : str(access_token)
    }
    print(f"get_acess_token_time() finished in {time.time() - start}")


def check_password_time(user, password):
    start = time.time()
    passed = check_password(password, user.password)
    print(passed)
    print(f"check_password_time() finished in {time.time() - start}")

