from django.urls import include, path
from rest_framework import routers

from mobile_service.views import CompanyView, MobileCategoryView, MobileView

router = routers.DefaultRouter()
router.register("category", MobileCategoryView, basename="category")
router.register("company", CompanyView, basename="company")
router.register("", MobileView, basename="mobile")

urlpatterns = [
    path("", include(router.urls)),
]
