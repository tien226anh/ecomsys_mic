from django.shortcuts import render
from rest_framework import viewsets

from book_service.models import (
    BookModel,
    BookCategoryModel,
    AuthorModel,
    PublisherModel,
)
from book_service.serializers import (
    BookSerializer,
    BookCategorySerializer,
    AuthorSerializer,
    PublisherSerializer,
)


# Create your views here.
class CategoryView(viewsets.ModelViewSet):
    queryset = BookCategoryModel.objects.all()
    serializer_class = BookCategorySerializer


class AuthorView(viewsets.ModelViewSet):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer


class PublisherView(viewsets.ModelViewSet):
    queryset = PublisherModel.objects.all()
    serializer_class = PublisherSerializer


class BookView(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
