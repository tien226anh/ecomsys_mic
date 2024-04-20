from rest_framework import serializers

from book_service.models import (
    AuthorModel,
    BookModel,
    BookCategoryModel,
    PublisherModel,
)


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherModel
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = "__all__"


class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategoryModel
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = "__all__"
