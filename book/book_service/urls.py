from django.urls import include, path
from rest_framework import routers

from book_service.views import AuthorView, BookView, CategoryView, PublisherView

router = routers.DefaultRouter()
router.register("category", CategoryView, basename="category")
router.register("author", AuthorView, basename="author")
router.register("publisher", PublisherView, basename="publisher")
router.register("", BookView, basename="book")

urlpatterns = [
    path("", include(router.urls)),
]
