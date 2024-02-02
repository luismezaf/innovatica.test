from django.contrib import admin
from apps.products.models import Product, ProductCategory, ProductPicture


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'state',
    )


@admin.register(ProductPicture)
class ProductPictureAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image'
    )
