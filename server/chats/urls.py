from django.urls import path
from chats.views import *

urlpatterns = [
    path("get-messages/", GetMessagesInChatRoom.as_view()),
    path("send-message/", SendMessage.as_view()),
    path("start-message-user/", StartMessageUser.as_view())
]