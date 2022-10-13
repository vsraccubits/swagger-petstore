from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiResponse,
    extend_schema,
    extend_schema_view,
)

"""
API response example of InventoryAPIView.
    path: stores.api.view.InventoryAPIView
"""
inventory_api_response = {
    "available": "string",
    "pending": "string",
    "sold": "string",
}

"""
OrderSerializer example
    path: stores.api.serializers.OrderSerializer
"""
order_serializer_response = {
    "id": 0,
    "quantity": 0,
    "ship_date": "2022-10-13T15:25:32.425Z",
    "status": "placed",
    "complete": True,
    "pet": 0,
}


def swagger_inventory_apiview():
    """
    Return extend_schema_view of drf-spectacular on InventoryAPIView.
        path: stores.api.view.InventoryAPIView
    """

    return extend_schema_view(
        get=extend_schema(
            summary="Returns pet inventories by status",
            description="Returns a map of status codes to quantities",
            responses={
                200: OpenApiResponse(
                    description="Successful operation",
                    response=OpenApiTypes.OBJECT,
                    examples=[
                        OpenApiExample(
                            "success",
                            value=inventory_api_response,
                            status_codes=["200"],
                        )
                    ],
                )
            },
        ),
    )


def swagger_order_createmixin():
    """
    Return extend_schema_view of drf-spectacular on OrderCreateMixin.
        path: stores.api.view.OrderCreateMixin
    """

    return extend_schema_view(
        post=extend_schema(
            summary="Place an order for a pet",
            description="Place a new order in the store",
            responses={
                200: OpenApiResponse(
                    description="Successful operation",
                    response=OpenApiTypes.OBJECT,
                    examples=[
                        OpenApiExample(
                            "success",
                            value=order_serializer_response,
                            status_codes=["200"],
                        )
                    ],
                ),
                400: OpenApiResponse(description="Invalid input"),
            },
        ),
    )


def swagger_order_retrivedestroy():
    """
    Return extend_schema_view of drf-spectacular on OrderRetrieveDestroyAPIView.
        path: stores.api.view.OrderRetrieveDestroyAPIView
    """

    return extend_schema_view(
        get=extend_schema(
            summary="Find purchase order by ID",
            description="Retrive order by ID.",
            responses={
                200: OpenApiResponse(
                    description="Successful operation",
                    response=OpenApiTypes.OBJECT,
                    examples=[
                        OpenApiExample(
                            "success",
                            value=order_serializer_response,
                            status_codes=["200"],
                        )
                    ],
                ),
                404: OpenApiResponse(description="Order not found"),
            },
        ),
        delete=extend_schema(
            summary="Delete purchase order by ID",
            description="Delete an order by ID.",
            responses={
                204: OpenApiResponse(description="No response body"),
                404: OpenApiResponse(description="Order not found"),
            },
        ),
    )
