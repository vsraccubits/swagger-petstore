from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from pets import models
from pets.api import serializers
from swaggerpetstore.core import constants
from swaggerpetstore.core.swagger import pets


@pets.swagger_pet_by_tags()
@api_view(["GET"])
def pet_by_tags(request):
    """
    View return list of Pets, by filtering against tags query parameter in the URL.
    This api accept multiple tags as query parameneter.
        eg: http://base_url/api/v1/pet/findByTags?tags=tag1&tags=tag2
    """

    if request.method == "GET":
        query_params = request.query_params.getlist("tags")
        if query_params == (None or []):
            return Response(
                constants.MESSAGES["INVALID_QUERYPARAM"],
                status=status.HTTP_400_BAD_REQUEST,
            )
        tags = models.Tag.objects.values_list("id", flat=True).filter(
            name__in=query_params
        )
        if not tags:
            return Response(
                constants.MESSAGES["INVALID_QUERYPARAM"],
                status=status.HTTP_400_BAD_REQUEST,
            )
        queryset = models.Pet.objects.filter(tags__in=tags).distinct()
        for tag in tags:
            queryset = queryset.filter(tags=tag)
        serializer = serializers.PetSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@pets.swagger_pet_by_status()
class PetByStatusAPIView(APIView):
    """
    View return list of Pets, by filtering against a status query parameter in the URL.
    """

    def get(self, request):
        query_params = self.request.query_params.get("status")
        if query_params not in models.Pet.PetStatuses:
            return Response(
                constants.MESSAGES["INVALID_QUERYPARAM"],
                status=status.HTTP_400_BAD_REQUEST,
            )
        queryset = models.Pet.objects.filter(status=query_params)
        serializer = serializers.PetSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
