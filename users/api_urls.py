from django.urls import path

from users.api import views

urlpatterns = [
    path("", views.UserCreateAPIView.as_view()),
    path("<str:userName>/", views.UserRetriveUpdateDestroyAPIView.as_view()),
]
