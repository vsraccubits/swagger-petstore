from django.urls import path

from stores.api import views

urlpatterns = [
    path("inventory/", views.InventoryAPIView.as_view()),
    path("order/", views.OrderCreateMixin.as_view()),
    path("order/<int:orderId>/", views.OrderRetrieveDestroyAPIView.as_view()),
]
