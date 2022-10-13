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

"""
PetSerializer example
    path: pets.api.serializers.PetSerializer
"""
pet_serializer_response = {
    "id": 0,
    "name": "string",
    "category": {"id": 0, "name": "string"},
    "photoUrls": ["string"],
    "tags": [{"id": 0, "name": "string"}],
    "status": "string",
}


def swagger_pet_modelviewset():
    """
    Return extend_schema_view of drf-spectacular on PetModelViewSet.
        path: pets.api.viewsets.PetModelViewSet
    """

    return extend_schema_view(
        list=extend_schema(
            exclude=True,
        ),
        retrieve=extend_schema(
            summary="Find pet by ID",
            description="Returns a single pet",
            responses={
                200: OpenApiResponse(
                    description="Successful operation",
                    response=OpenApiTypes.OBJECT,
                    examples=[
                        OpenApiExample(
                            "success",
                            value=pet_serializer_response,
                            status_codes=["200"],
                        )
                    ],
                ),
                400: OpenApiResponse(description="Invalid ID supplied"),
                404: OpenApiResponse(description="Pet not found"),
            },
        ),
        create=extend_schema(
            summary="Add a new pet to the store",
            description="Add a new pet to the store",
            responses={
                201: OpenApiResponse(
                    description="Successful operation",
                    response=OpenApiTypes.OBJECT,
                    examples=[
                        OpenApiExample(
                            "success",
                            value=pet_serializer_response,
                            status_codes=["201"],
                        )
                    ],
                ),
                404: OpenApiResponse(description="Bad Request"),
            },
        ),
        update=extend_schema(
            summary="Update an existing pet",
            description="Update an existing pet by Id",
            responses={
                200: OpenApiResponse(
                    description="Successful operation",
                    response=OpenApiTypes.OBJECT,
                    examples=[
                        OpenApiExample(
                            "success",
                            value=pet_serializer_response,
                            status_codes=["200"],
                        )
                    ],
                ),
                400: OpenApiResponse(description="Invalid ID supplied"),
                404: OpenApiResponse(description="Pet not found"),
                405: OpenApiResponse(description="Validation exception"),
            },
        ),
        partial_update=extend_schema(
            summary="Partially update an existing pet",
            description="Update fields of an existing pet by Id",
            deprecated=True,
        ),
        destroy=extend_schema(
            summary="Deletes a pet",
            responses={
                204: OpenApiResponse(description="No response body"),
                400: OpenApiResponse(description="Invalid pet value"),
            },
        ),
        upload_image=extend_schema(
            summary="Uploads an image",
            request={
                "multipart/form-data": {
                    "type": "object",
                    "properties": {
                        "photo": {"type": "string", "format": "binary"},
                    },
                },
            },
            responses={
                200: OpenApiResponse(
                    description="Successful operation",
                    response=OpenApiTypes.OBJECT,
                    examples=[
                        OpenApiExample(
                            "success",
                            value=api_response(
                                200, constants.SUCCESS_RESPONSE, pet_serializer_response
                            ),
                            status_codes=["200"],
                        )
                    ],
                ),
                400: OpenApiResponse(description="Invalid ID supplied"),
                404: OpenApiResponse(description="Pet not found"),
            },
        ),
    )


def swagger_pet_viewset():
    """
    Return extend_schema_view of drf-spectacular on PetViewSet.
        path: pets.api.viewsets.PetViewSet
    """

    return extend_schema_view(
        partial_update=extend_schema(
            summary="Updates a pet in the store with form data",
            request=None,
            parameters=[
                OpenApiParameter(
                    "petId",
                    OpenApiTypes.STR,
                    OpenApiParameter.PATH,
                    required=True,
                    description="ID of pet that needs to be updated",
                ),
                OpenApiParameter(
                    "name",
                    OpenApiTypes.STR,
                    OpenApiParameter.QUERY,
                    description="Name of pet that needs to be updated",
                ),
                OpenApiParameter(
                    "status",
                    OpenApiTypes.STR,
                    OpenApiParameter.QUERY,
                    description="Status of pet that needs to be updated",
                ),
            ],
            responses={
                200: OpenApiResponse(
                    description="Successful operation",
                    response=OpenApiTypes.OBJECT,
                    examples=[
                        OpenApiExample(
                            "success",
                            value=pet_serializer_response,
                            status_codes=["200"],
                        )
                    ],
                ),
                400: OpenApiResponse(description="Invalid input"),
                404: OpenApiResponse(description="Pet not found"),
            },
        ),
    )


def swagger_pet_by_tags():
    """
    Return extend_schema_view of drf-spectacular on pet_by_tags.
        path: pets.api.view.pet_by_tags
    """

    return extend_schema_view(
        get=extend_schema(
            summary="Find Pets by tags",
            description="Multiple tags can be provided with comma separated strings. \
                Use tag1, tag2, tag3 for testing.",
            parameters=[
                OpenApiParameter(
                    "tags",
                    type={"type": "array", "items": {"type": "string"}},
                    location=OpenApiParameter.QUERY,
                    description="Tags to filter by",
                )
            ],
            responses={
                200: OpenApiResponse(
                    description="Successful operation",
                    response=OpenApiTypes.OBJECT,
                    examples=[
                        OpenApiExample(
                            "success",
                            value=[pet_serializer_response],
                            status_codes=["200"],
                        )
                    ],
                ),
                400: OpenApiResponse(description="Invalid tag value"),
            },
        ),
    )


def swagger_pet_by_status():
    """
    Return extend_schema_view of drf-spectacular on PetByStatusAPIView.
        path: pets.api.view.PetByStatusAPIView
    """

    return extend_schema_view(
        get=extend_schema(
            summary="Find Pets by status",
            description="Multiple status values can be provided with comma separated strings",
            parameters=[
                OpenApiParameter(
                    "status",
                    OpenApiTypes.STR,
                    OpenApiParameter.QUERY,
                    enum=["available", "pending", "sold"],
                    description="Status values that need to be considered for filter",
                )
            ],
            responses={
                200: OpenApiResponse(
                    description="Successful operation",
                    response=OpenApiTypes.OBJECT,
                    examples=[
                        OpenApiExample(
                            "success",
                            value=[pet_serializer_response],
                            status_codes=["200"],
                        )
                    ],
                ),
                400: OpenApiResponse(description="Invalid status value"),
            },
        ),
    )
