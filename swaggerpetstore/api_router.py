from django.urls import include, path
from drf_spectacular import views

urlpatterns = [
    path("pet/", include("pets.api_urls")),
    path("store/", include("stores.api_urls")),
    path("user/", include("users.api_urls")),
    path("schema/", views.SpectacularAPIView.as_view(), name="schema"),
    path(
        "", views.SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"
    ),
    path(
        "redoc/",
        views.SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
