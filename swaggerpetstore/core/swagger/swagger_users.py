from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiParameter,
    OpenApiResponse,
    extend_schema,
    extend_schema_view,
)

from swaggerpetstore.core import constants
from swaggerpetstore.core.utils import api_response
from users.api.serializers import UserSerializer

"""
UserSerializer example
    path: users.api.serializers.UserSerializer
"""
user_serializer_response = {
    "id": 0,
    "username": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "swagger@email.com",
    "password": "12345",
    "phone": "string",
    "userStatus": 1,
}


def swagger_users_create():
    """
    Return extend_schema_view of drf-spectacular on UserCreateAPIView.
        path: users.api.view.UserCreateAPIView
    """

    return extend_schema_view(
        post=extend_schema(
            summary="Create user",
            description="This can only be done by the logged in user.",
            responses={
                200: OpenApiResponse(
                    description="Successful operation",
                    response=UserSerializer,
                ),
                400: OpenApiResponse(description="Invalid input"),
                401: OpenApiResponse(description="Unauthorized"),
            },
        ),
    )


def swagger_users_retriveupdatedestroy():
    """
    Return extend_schema_view of drf-spectacular on UserRetriveUpdateDestroyAPIView.
        path: users.api.view.UserRetriveUpdateDestroyAPIView
    """

    return extend_schema_view(
        get=extend_schema(
            summary="Get user by username",
            responses={
                200: OpenApiResponse(
                    description="Successful operation",
                    response=UserSerializer,
                ),
                401: OpenApiResponse(description="Unauthorized"),
                404: OpenApiResponse(description="User not found"),
            },
        ),
        put=extend_schema(
            summary="Update user",
            description="This can only be done by the logged in user.",
            responses={
                200: OpenApiResponse(
                    description="Successful operation",
                    response=UserSerializer,
                ),
                401: OpenApiResponse(description="Unauthorized"),
                404: OpenApiResponse(description="User not found"),
            },
        ),
        patch=extend_schema(exclude=True),
        delete=extend_schema(
            summary="Delete user",
            description="This can only be done by the logged in user.",
            responses={
                204: OpenApiResponse(description="No response body"),
                401: OpenApiResponse(description="Unauthorized"),
                404: OpenApiResponse(description="User not found"),
            },
        ),
    )


def swagger_user_login_apiview():
    """
    Return extend_schema_view of drf-spectacular on UserLoginAPIView.
        path: users.api.view.UserLoginAPIView
    """

    return extend_schema_view(
        get=extend_schema(
            summary="Logs user into the system",
            parameters=[
                OpenApiParameter(
                    "username",
                    OpenApiTypes.STR,
                    OpenApiParameter.QUERY,
                    description="The user name for login",
                ),
                OpenApiParameter(
                    "password",
                    OpenApiTypes.STR,
                    OpenApiParameter.QUERY,
                    description="The password for login in clear text",
                ),
            ],
            responses={
                200: OpenApiResponse(
                    description="Successful operation",
                    response=OpenApiTypes.OBJECT,
                    examples=[
                        OpenApiExample(
                            "success",
                            value={"token": "string"},
                            status_codes=["200"],
                        )
                    ],
                ),
                400: OpenApiResponse(description="Invalid username/password supplied"),
            },
        ),
    )


def swagger_user_logout_apiview():
    """
    Return extend_schema_view of drf-spectacular on UserLogoutAPIView.
        path: users.api.view.UserLogoutAPIView
    """

    return extend_schema_view(
        post=extend_schema(
            summary="Logs out current logged in user session",
            request=None,
            responses={
                200: OpenApiResponse(description="Successful operation"),
                400: OpenApiResponse(description="Not logged in"),
                401: OpenApiResponse(description="Unauthorized"),
            },
        ),
    )


def swagger_users_listcreate():
    """
    Return extend_schema_view of drf-spectacular on UserListCreateAPIView.
        path: users.api.view.UserListCreateAPIView
    """

    return extend_schema_view(
        post=extend_schema(
            summary="Create list of users with given input array",
            description="Creates list of users with given input array",
            request=UserSerializer(many=True),
            responses={
                200: OpenApiResponse(
                    description="Successful operation",
                    response=OpenApiTypes.OBJECT,
                    examples=[
                        OpenApiExample(
                            "success",
                            value=api_response(
                                200,
                                constants.SUCCESS_RESPONSE,
                                [user_serializer_response],
                            ),
                            status_codes=["200"],
                        )
                    ],
                ),
                400: OpenApiResponse(description="Invalid input"),
            },
        ),
    )
