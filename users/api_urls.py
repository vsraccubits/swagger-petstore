from django.urls import path

from users.api import views

urlpatterns = [
    path("", views.UserCreateAPIView.as_view()),
    path("<str:userName>/", views.UserRetriveUpdateDestroyAPIView.as_view()),
    path("auth/login/", views.UserLoginAPIView.as_view()),
    path("auth/logout/", views.UserLogoutAPIView.as_view()),
    path("create/createWithList/", views.UserListCreateAPIView.as_view()),
]
