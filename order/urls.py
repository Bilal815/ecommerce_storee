from django.urls import path
from . import views


urlpatterns = [
    path("api/order/<int:pk>/", views.OrderView.as_view()),
    path("api/payment/", views.Payment),
]
