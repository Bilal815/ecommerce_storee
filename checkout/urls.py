from django.urls import path
from . import views


urlpatterns = [
    path("api/checkout/<int:pk>/", views.CheckoutView.as_view()),
    path("api/cart/checkout/<int:pk>/", views.CheckoutCartView.as_view()),
]
