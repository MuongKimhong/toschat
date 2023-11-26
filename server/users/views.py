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
        print(data)
 
        if User.objects.filter(username=data["username"]).exists() is True:
            return Response({"username_taken": True}, status=400)

        User.objects.create(username=data["username"], password=make_password(data["password"]))
        return Response({"signup_success": True}, status=200)


class ListAllUsers(APIView):
    permission_classes = [ IsAuthenticated ]

    def get(self, request):
        if User.objects.all().count() > 15:
            users = list(User.objects.all().exclude(id=request.query_params["current_user_id"]))[:15]
        else:
            users = User.objects.all().exclude(id=request.query_params["current_user_id"])

        users = [user.serialize() for user in users]
        return Response({"users": users}, status=200)


class SearchUser(APIView):
    permission_classes = [ IsAuthenticated ]

    def get(self, request):
        users = User.objects.filter(username__icontains=request.query_params["search_text"])
        users = users.exclude(id=int(request.query_params["current_user_id"]))
        users = [user.username for user in users]

        return Response({"users": users}, status=200)
