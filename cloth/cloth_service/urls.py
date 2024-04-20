from django.urls import include, path
from rest_framework import routers

from cloth_service.views import ClothView, ClothCategoryView, ManufacturerView

router = routers.DefaultRouter()
router.register("category", ClothCategoryView, basename="category")
router.register("manufacturer", ManufacturerView, basename="manufacturer")
router.register("", ClothView, basename="cloth")

urlpatterns = [
    path("", include(router.urls)),
]
