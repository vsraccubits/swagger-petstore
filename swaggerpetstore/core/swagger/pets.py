from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiExample, extend_schema, extend_schema_view

from drf_spectacular.utils import OpenApiResponse  # isort:skip


def swagger_pet_modelviewset():
    """
    Return schema for PetModelViewSet.
        location: pets/api/viewsets/PetModelViewSet
    """

    pet_response = {
        "id": 0,
        "name": "string",
        "category": {"id": 0, "name": "string"},
        "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": "string",
    }

    return extend_schema_view(
        list=extend_schema(
            exclude=True,
        ),
        retrieve=extend_schema(
            summary="Find pet by ID",
            description="Returns a single pet",
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
                            "success", value=pet_response, status_codes=["201"]
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
                            "success", value=pet_response, status_codes=["200"]
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
        ),
    )


def swagger_pet_viewset():
    """
    Return schema for PetViewSet.
        location: pets/api/viewsets/PetViewSet
    """

    return extend_schema_view(
        partial_update=extend_schema(
            summary="Updates a pet in the store with form data",
        ),
    )


def swagger_pet_by_tags():
    """
    Return schema for pet_by_tags.
        location: pets/api/view/pet_by_tags
    """

    return extend_schema_view(
        get=extend_schema(
            summary="Find Pets by tags",
            description="Multiple tags can be provided with comma separated strings. \
                Use tag1, tag2, tag3 for testing.",
        ),
    )


def swagger_pet_by_status():
    """
    Return schema for PetByStatusAPIView.
        location: pets/api/view/PetByStatusAPIView
    """

    return extend_schema_view(
        get=extend_schema(
            summary="Find Pets by status",
            description="Multiple status values can be provided with comma separated strings",
        ),
    )
