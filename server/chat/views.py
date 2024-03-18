from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import User, UserContact
from chat.models import ChatRoom, Message


class GetMessages(APIView):
    permission_classes = [ IsAuthenticated ]

    def get(self, request):
        data = request.query_params
        try:
            chatroom = ChatRoom.objects.get(id=data["chatroom_id"])
        except ChatRoom.DoesNotExist:
            return Response({"chatroom_not_exist": True}, status=400)

        if request.user not in chatroom.members.all():
            return Response({"user_not_in_room": True}, status=400)

        messages = Message.objects.filter(chatroom__id=chatroom.id)
        messages = [message.serialize() for message in messages]
        return Response({"messages": messages}, status=200)


class SendMessage(APIView):
    permission_classes = [ IsAuthenticated ]

    def post(self, request):
        try:
            chatroom = ChatRoom.objects.get(id=request.data["chatroom_id"])
        except ChatRoom.DoesNotExist:
            return Response({"chatroom_not_exist": True}, status=400)

        if request.user not in chatroom.members.all():
            return Response({"user_not_in_room": True}, status=400)

        message = Message.objects.create(
            chatroom_id=chatroom.id,
            sender_id=request.user.id,
            text=request.data["text"]
        )
        message = message.serialize()

        for member in chatroom.members.all():
            if member.id != request.user.id:
                message["receiver"] = member.serialize()

        return Response({"new_message": message}, status=200)
