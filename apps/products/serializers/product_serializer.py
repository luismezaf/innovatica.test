
from typing import TYPE_CHECKING

from rest_framework import serializers

from apps.products.models import Product
from apps.products.serializers.product_category_serializer import ProductCategorySerializer

if TYPE_CHECKING:
    from apps.products.models import ProductPicture


class AllowAnyProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            'id',
            'name',
            'state',
        ]
        model = Product


class WriteProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            'id',
            'name',
            'state',
            'categories'
        ]
        model = Product


class ReadProductSerializer(serializers.ModelSerializer):
    categories = ProductCategorySerializer(many=True)
    pictures = serializers.SerializerMethodField(read_only=True)

    def get_pictures(self, instance: 'Product'):
        images_url = []
        for picture in instance.pictures.all():
            picture: 'ProductPicture'
            images_url.append(picture.image.url)
        return images_url

    class Meta:
        fields = [
            'id',
            'name',
            'state',
            'categories',
            'pictures'
        ]
        model = Product


class FilteredReadProductSerializer(ReadProductSerializer):
    picture = serializers.SerializerMethodField()

    def get_picture(self, instance: 'Product'):
        return instance.picture.image.url if instance.picture else None

    class Meta:
        fields = [
            'id',
            'name',
            'state',
            'categories',
            'picture'
        ]
        model = Product
