from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView

from stores import models
from stores.api import serializers


class InventoryAPIView(APIView):
    """
    View return pet count by status.
    """

    def get(self, request):
        available = models.Pet.objects.filter(status="available").count()
        pending = models.Pet.objects.filter(status="pending").count()
        sold = models.Pet.objects.filter(status="sold").count()
        response = {"available": available, "pending": pending, "sold": sold}
        return Response(response, status=status.HTTP_200_OK)


class OrderCreateMixin(mixins.CreateModelMixin, generics.GenericAPIView):
    """
    Mixin to create an order.
    """

    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OrderRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    """
    GenericAPIView Retrive, Delete an order by orderId.
    """

    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    lookup_url_kwarg = "orderId"
