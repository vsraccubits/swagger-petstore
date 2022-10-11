from django.contrib.auth import authenticate, get_user_model, login, logout
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from swaggerpetstore.core import constants, utils
from users.api import serializers

User = get_user_model()


class UserCreateAPIView(generics.CreateAPIView):
    """
    GenericAPIView create a user.
    """

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    GenericAPIView Retrive, Update, Delete user by username.
    """

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    lookup_field = "username"
    lookup_url_kwarg = "userName"
    permission_classes = [IsAuthenticated]


class UserLoginAPIView(APIView):
    """
    View logged user into the system.
    """

    def get(self, request):
        username = request.query_params.get("username")
        password = request.query_params.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.user_status != User.UserStatuses.BLOCKED:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                response = {"token": token.key}
                return Response(response, status=status.HTTP_200_OK)
            else:
                return Response(
                    constants.MESSAGES["FORBIDDEN"], status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                constants.MESSAGES["INVALID_CREDENTIALS"],
                status=status.HTTP_400_BAD_REQUEST,
            )


class UserLogoutAPIView(APIView):
    """
    View logout current loggedin user.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.is_authenticated:
            try:
                request.user.auth_token.delete()
            except (AttributeError, ObjectDoesNotExist):
                pass
            logout(request)
            return Response(
                constants.MESSAGES["SUCCESS_LOGOUT"], status=status.HTTP_200_OK
            )
        else:
            return Response(
                constants.MESSAGES["NOT_LOGGED_IN"], status=status.HTTP_400_BAD_REQUEST
            )


class UserListCreateAPIView(APIView):
    """
    View create list of user from given input list.
    """

    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            response = utils.api_response(
                status.HTTP_200_OK, constants.SUCCESS_RESPONSE, serializer.data
            )
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = utils.api_response(
                status.HTTP_400_BAD_REQUEST,
                constants.ERRROR_RESPONSE,
                serializer.errors,
            )
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
