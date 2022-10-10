from django.urls import path
from rest_framework import routers

from pets.api import views, viewsets

router = routers.SimpleRouter()
router.register(r"", viewsets.PetModelViewSet)
router.register(r"formdata", viewsets.PetViewSet, basename="formdata")

urlpatterns = [
    path("findByStatus/", views.PetByStatusAPIView.as_view()),
    path("findByTags/", views.pet_by_tags),
]

urlpatterns += router.urls
