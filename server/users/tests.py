from django.contrib.auth.hashers import make_password
from users.models import User


def create_dummy_users(number_of_user: int) -> None:
    for i in range(number_of_user):
        print(f"Creating user {i}")
        user = User.objects.create(
            username=f"user{i}",
            password=make_password("12345")
        )

    print("Finished") 

