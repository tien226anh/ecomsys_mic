from rest_framework import serializers

from mobile_service.models import MobileCompanyModel, MobileCategoryModel, MobileModel


class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileModel
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileCompanyModel
        fields = "__all__"


class MobileCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileCategoryModel
        fields = "__all__"
