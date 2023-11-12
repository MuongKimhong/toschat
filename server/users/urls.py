from django.urls import path
from users.views import *

urlpatterns = [
    path("sign-in/", SignIn.as_view()),
    path("sign-up/", SIgnUp.as_view()),
    path("list-all-users/", ListAllUsers.as_view())
]