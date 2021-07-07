from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CountryViewSet,
    CategoryViewSet,
    ItemVariantViewSet,
    ReviewViewSet,
    ItemViewSet,
)

router = DefaultRouter()
router.register("review", ReviewViewSet)
router.register("itemvariant", ItemVariantViewSet)
router.register("country", CountryViewSet)
router.register("category", CategoryViewSet)
router.register("item", ItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
