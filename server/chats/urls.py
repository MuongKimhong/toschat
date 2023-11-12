from django.urls import path
from chats.views import *

urlpatterns = [
    path("get-messages/", GetMessagesInChatRoom.as_view())
]