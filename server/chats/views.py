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
        other_user = User.objects.get(username=request.data["other_username"])

        print(current_user)
        print(other_user)

        query = ChatRoom.objects.filter(members=current_user).filter(members=other_user)

        if query.exists():
            chatroom = query.first()
        else:
            chatroom = ChatRoom.objects.create()
            chatroom.members.add(current_user)
            chatroom.members.add(other_user)

        print(chatroom)

        return Response({"chatroom_id": chatroom.id}, status=200)


class GetChatRoomDetail(APIView):
    permission_classes = [ IsAuthenticated ]

    def get(self, request):
        chatroom = ChatRoom.objects.get(id=int(request.query_params["chatroom_id"]))
        return Response({"chatroom": chatroom.serialize()}, status=200)
