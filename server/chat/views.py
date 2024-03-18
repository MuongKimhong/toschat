from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.models import ChatRoom, Message

import time


class GetMessages(APIView):
    permission_classes = [ IsAuthenticated ]

    def group_messages_by_date(self, messages):
        '''
        100 messages take 0.05s to finish this function
        '''
        serialized_messages = []
        all_dates = []

        for message in messages:
            date_str = message.created_date.date().strftime('%d/%m/%Y')

            if date_str not in all_dates:
                all_dates.append(date_str)

        for date in all_dates:
            serialized_messages.append({
                "type": "date", 
                "message": {"id": 0, "text": date} 
            })
            for message in messages:
                msg_date_str = message.created_date.date().strftime('%d/%m/%Y')

                if msg_date_str == date:
                    serialized_messages.append(message.serialize())
                    messages.exclude(id=message.id)

        return serialized_messages

    def get(self, request):
        data = request.query_params
        try:
            chatroom = ChatRoom.objects.get(id=data["chatroom_id"])
        except ChatRoom.DoesNotExist:
            return Response({"chatroom_not_exist": True}, status=400)

        if request.user not in chatroom.members.all():
            return Response({"user_not_in_room": True}, status=400)

        messages = Message.objects.filter(chatroom__id=chatroom.id)
        messages = self.group_messages_by_date(messages)
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
                break

        return Response({"new_message": message}, status=200)
