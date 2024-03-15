from django.urls import path

from account.views import *

urlpatterns = [
    path("sign-in/", SignIn.as_view()),
    path("sign-up/", SignUp.as_view()),
    path("get-all-contacts/", GetAllContacts.as_view()),
    path("add-new-contact/", AddNewContact.as_view()),
    path("search-contacts/", SearchContacts.as_view()),
    path("search-users-by-username/", SearchUsersByUsername.as_view())
]