import os

from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.response import Response

from pets import models
from pets.api import serializers
from swaggerpetstore.core import constants, utils
from swaggerpetstore.core.swagger import swagger_pets


@swagger_pets.swagger_pet_modelviewset()
class PetModelViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for viewing and editing pet model.
    """

    queryset = models.Pet.objects.all()
    serializer_class = serializers.PetSerializer
    lookup_url_kwarg = "petId"
    parser_classes = [JSONParser, MultiPartParser]

    def perform_destroy(self, instance):
        category = instance.category
        tags = instance.tags.all()
        photo_urls = instance.photo_urls.all()
        if tags:
            for tag in tags:
                tag.delete()
        if photo_urls:
            for photo_url in photo_urls:
                path = os.path.join(settings.MEDIA_ROOT, photo_url.photo.name)
                if os.path.exists(path):
                    os.remove(path)
                photo_url.delete()
        instance.delete()

        # Since category is PROTECTED, It has to delete after deletion of refernce object.
        if category:
            category.delete()

    @action(detail=True, methods=["POST"], url_path="uploadImage")
    def upload_image(self, request, petId=None):
        """
        Extra action to upload pet image.
        """

        pet = get_object_or_404(models.Pet, pk=petId)
        file = request.FILES.get("photo")
        data = {"photo": file}
        if pet:
            serializer = serializers.PhotoUrlsSerializer(data=data)
            if serializer.is_valid():
                photo_url = models.PhotoUrl.objects.create(photo=file)
                photo_url.save()
                pet.photo_urls.add(photo_url)
                pet.save()
                serializer = serializers.PetSerializer(pet)
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


@swagger_pets.swagger_pet_viewset()
class PetViewSet(viewsets.ViewSet):
    """
    Viewset for partially update name and status of a Pet.
    """

    serializer_class = serializers.PetSerializer
    parser_classes = [FormParser]
    lookup_url_kwarg = "petId"

    def partial_update(self, request, petId=None):
        pet = get_object_or_404(models.Pet, pk=petId)
        pet_name = request.query_params.get("name")
        pet_status = request.query_params.get("status")
        if pet_name and (pet_status in models.Pet.PetStatuses):
            pet.name = pet_name
            pet.status = pet_status
            pet.save()
            serializer = serializers.PetSerializer(pet)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                constants.MESSAGES["INVALID_QUERYPARAM"],
                status=status.HTTP_400_BAD_REQUEST,
            )
