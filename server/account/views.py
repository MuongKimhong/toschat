from django.contrib.auth.hashers import make_password, check_password
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import User, UserContact
from chat.models import ChatRoom


def get_token(user) -> dict:
    refresh_token = RefreshToken.for_user(user) 
    access_token  = refresh_token.access_token
    data = {
        'user': user.serialize(),
        'refresh_token': str(refresh_token),
        'access_token' : str(access_token)
    }
    return data


class SignIn(APIView):
    permission_classes = [ AllowAny ]

    def post(self, request):
        try:
            user = User.objects.get(username=request.data["username"])
        except User.DoesNotExist:
            return Response({"error": True}, status=400)

        if check_password(request.data["password"], user.password) is False:
            return Response({"error": True}, status=400)

        return Response(get_token(user), status=200)


class SignUp(APIView):
    permission_classes = [ AllowAny ]

    def post(self, request):
        data = request.data

        if len(data["password"]) < 8:
            return Response({"password_length_err": "Password should be at least 8 characters"}, status=400)

        elif data["password"] != data["confirm_password"]:
            return Response({"password_not_match": "Two password did not match"}, status=400)
 
        try:
            user = User.objects.get(username=data["username"])
            return Response({"username_taken": "Username is already taken"}, status=400)
        except User.DoesNotExist:
            user = User.objects.create(
                username=data["username"],
                password=make_password(data["password"])
            )

        return Response({"success": True}, status=200)


class GetAllContacts(APIView):
    permission_classes = [ IsAuthenticated ]

    def get(self, request):
        contacts = UserContact.objects.filter(user__id=request.user.id)
        contacts = [contact.serialize()["contact"] for contact in contacts]
        return Response({"contacts": contacts}, status=200)


class AddNewContact(APIView):
    permission_classes = [ IsAuthenticated ]

    def create_contact(self, user_id: int, contact_id: int) -> UserContact:
        new_contact = UserContact.objects.create(user_id=user_id, contact_id=contact_id)
        return new_contact

    def post(self, request):
        try:
            contact = User.objects.get(username=request.data["contact_username"])
        except User.DoesNotExist:
            return Response({"contact_not_exist": True}, status=400)
        
        try:
            user_contact = UserContact.objects.get(user__id=request.user.id, contact__id=contact.id)
        except UserContact.DoesNotExist:
            # create new contact for current user
            new_contact = self.create_contact(user_id=request.user.id, contact_id=contact.id)
            # create new contact for another user
            self.create_contact(user_id=contact.id, contact_id=request.user.id)

        # create new chatroom for both user
        if not ChatRoom.objects.filter(members__in=[request.user, contact]).exists():
            chatroom = ChatRoom.objects.create()
            chatroom.members.add(request.user, contact)

        return Response({"success": True}, status=200)


class SearchUsersByUsername(APIView):
    permission_classes = [ IsAuthenticated ]

    def get(self, request):
        search_text = request.query_params.get("search_text")
        if search_text is None:
            return Response({"param_missing": True}, status=400)

        search_results = User.objects.filter(username__icontains=search_text).exclude(id=request.user.id)
        search_results = [user.serialize() for user in search_results]
        return Response({"results": search_results}, status=200)


class SearchContacts(APIView):
    permission_classes = [ IsAuthenticated ]

    def get(self, request):        
        text = request.query_params.get("search_text")
        if text is None:
            return Response({"param_missing": True}, status=400)

        results = UserContact.objects.filter(user__id=request.user.id, contact__username__icontains=text) 
        results = [contact.serialize()["contact"] for contact in results]
        return Response({"results": results}, status=200)
