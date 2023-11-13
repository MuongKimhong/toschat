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


class StartMessageUser(APIView):
    permission_classes = [ IsAuthenticated ]

    def post(self, request):
        current_user = User.objects.get(id=int(extract_user_id(request)))
        other_user = User.objects.get(id=int(request.data["other_user_id"]))

        if ChatRoom.objects.filter(members__in=[current_user.id, other_user.id]).exists():
            chatroom = ChatRoom.objects.get(members__in=[current_user.id, other_user.id])
        else:
            chatroom = ChatRoom.objects.create()
            chatroom.add(current_user)
            chatroom.add(other_user)

        return Response({"chatroom_id": chatroom.id}, status=200)
