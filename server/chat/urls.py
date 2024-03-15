from django.urls import path

from chat.views import *

urlpatterns = [
    path("get-messages/", GetMessages.as_view()),
    path("send-message/", SendMessage.as_view())
]