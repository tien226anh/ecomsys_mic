from django.shortcuts import render
from rest_framework import viewsets

from cloth_service.models import ClothCategoryModel, ClothModel, ClothManufacturerModel
from cloth_service.serializers import (
    ClothCategorySerializer,
    ClothSerializer,
    ManufacturerSerializer,
)


# Create your views here.
class ClothCategoryView(viewsets.ModelViewSet):
    queryset = ClothCategoryModel.objects.all()
    serializer_class = ClothCategorySerializer


class ManufacturerView(viewsets.ModelViewSet):
    queryset = ClothManufacturerModel.objects.all()
    serializer_class = ManufacturerSerializer


class ClothView(viewsets.ModelViewSet):
    queryset = ClothModel.objects.all()
    serializer_class = ClothSerializer
