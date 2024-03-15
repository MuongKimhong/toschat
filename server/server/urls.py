from django.urls import path, include


urlpatterns = [
    path("api-account/", include("account.urls")),
    path("api-chat/", include("chat.urls"))
]
