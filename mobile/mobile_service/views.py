from django.shortcuts import render
from rest_framework import viewsets

from mobile_service.models import MobileCompanyModel, MobileCategoryModel, MobileModel
from mobile_service.serializers import (
    CompanySerializer,
    MobileCategorySerializer,
    MobileSerializer,
)


# Create your views here.
class MobileCategoryView(viewsets.ModelViewSet):
    queryset = MobileCategoryModel.objects.all()
    serializer_class = MobileCategorySerializer


class CompanyView(viewsets.ModelViewSet):
    queryset = MobileCompanyModel.objects.all()
    serializer_class = CompanySerializer


class MobileView(viewsets.ModelViewSet):
    queryset = MobileModel.objects.all()
    serializer_class = MobileSerializer
