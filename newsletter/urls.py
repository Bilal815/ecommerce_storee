from rest_framework.routers import DefaultRouter
from .views import TagsViewSet, NewslettersViewSet, NewsletterListUser
from django.urls import path

router = DefaultRouter()
router.register('', TagsViewSet)
router.register('', NewslettersViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('mysubscriptions', NewsletterListUser.as_view(), name="newsletter")
]