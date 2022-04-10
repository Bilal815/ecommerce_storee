from django.urls import path
from . import views


urlpatterns = [
    path("api/cart/", views.CartItemAPIView.as_view()),
    path("api/cart-item/<int:pk>/", views.CartItemView.as_view()),
]
