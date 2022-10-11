from rest_framework import serializers

from stores import models


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for Order model.
    """

    class Meta:
        model = models.Order
        fields = "__all__"
