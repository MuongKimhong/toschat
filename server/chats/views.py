from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from chats.models import ChatRoom, Message
from users.utils import extract_user_id
from users.models import User


class GetMessagesInChatRoom(APIView):
    permission_classes = [ IsAuthenticated ]

    def get(self, request):
        messages = Message.objects.filter(chatroom__id=int(request.query_params["chatroom_id"]))
        messages = [message.serialize() for message in messages]

        return Response({"messages": messages}, status=200)


class SendMessage(APIView):
    permission_classes = [ IsAuthenticated ]

    def post(self, request):
        message = Message.objects.create(
            sender_id=extract_user_id(request),
            chatroom_id=request.data["chatroom_id"],
            text=request.data["text"]
        )
        return Response({"message": message.serialize()}, status=200)
