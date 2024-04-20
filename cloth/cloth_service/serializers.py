from rest_framework import serializers

from cloth_service.models import ClothCategoryModel, ClothModel, ClothManufacturerModel


class ClothCategorySerializer(serializers.Serializer):
    class Meta:
        model = ClothCategoryModel
        fields = "__all__"


class ManufacturerSerializer(serializers.Serializer):
    class Meta:
        model = ClothManufacturerModel
        fields = "__all__"


class ClothSerializer(serializers.Serializer):
    class Meta:
        model = ClothModel
        fields = "__all__"
