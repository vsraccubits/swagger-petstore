from django.urls import include, path

urlpatterns = [
    path("pet/", include("pets.api_urls")),
    path("store/", include("stores.api_urls")),
    path("user/", include("users.api_urls")),
]
