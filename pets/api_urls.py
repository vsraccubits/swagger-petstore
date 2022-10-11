from django.urls import path
from rest_framework import routers

from pets.api import views, viewsets

router = routers.SimpleRouter()
router.register(r"", viewsets.PetModelViewSet)
router.register(r"formdata", viewsets.PetViewSet, basename="formdata")

urlpatterns = [
    path("find/findByStatus/", views.PetByStatusAPIView.as_view()),
    path("find/findByTags/", views.pet_by_tags),
]

urlpatterns += router.urls
