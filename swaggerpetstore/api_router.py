from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("pet/", include("pets.api_urls")),
    path("store/", include("stores.api_urls")),
    path("user/", include("users.api_urls")),
    path("", TemplateView.as_view(template_name="swagger/swagger-ui.html")),
    path("redoc/", TemplateView.as_view(template_name="swagger/redoc.html")),
]
