
from rest_framework import serializers

from apps.products.models import ProductCategory


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            'id',
            'name',
        ]
        model = ProductCategory
