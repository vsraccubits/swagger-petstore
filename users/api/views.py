from django.contrib.auth import get_user_model
from rest_framework import generics

from users.api import serializers

User = get_user_model()


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    lookup_field = "username"
    lookup_url_kwarg = "userName"
