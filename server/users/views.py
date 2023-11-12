from django.contrib.auth.hashers import make_password, check_password
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User


def get_token(user):
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

        if data["password"] != data["confirm_password"]:
            return Response({"two_password_not_match": True}, status=400)
        
        if User.objects.filter(username=data["username"]).exists() is True:
            return Response({"username_taken": True}, status=400)

        User.objects.create(username=data["username"], password=make_password(data["password"]))
        return Response({"signup_success": True}, status=200)


class ListAllUsers(APIView):
    permission_classes = [ IsAuthenticated ]

    def get(self, request):
        users = User.objects.all().exclude(id=request.data["current_user_id"]).order_by("-id")
        users = [user.serialize() for user in users]

        return Response({"users": users}, status=200)
