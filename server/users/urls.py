from django.urls import path
from users.views import *

urlpatterns = [
    path("sign-in/", SignIn.as_view()),
    path("sign-up/", SignUp.as_view()),
    path("list-all-users/", ListAllUsers.as_view()),
    path("search-users/", SearchUser.as_view())
]