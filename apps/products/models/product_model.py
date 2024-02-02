
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.abstracts.abstract_model import BaseAbstractModel


PRODUCT_STATE_CHOICES = (
    ('in', "In stock"),
    ('na', "Not avaible"),
)


class ProductPicture(BaseAbstractModel):
    product = models.ForeignKey(
        'product',
        related_name='pictures',
        on_delete=models.CASCADE,
    )
    image = models.ImageField()

    class Meta:
        verbose_name = _("product picture")
        verbose_name_plural = _("product pictures")


class Product(BaseAbstractModel):
    name = models.CharField(
        _("product name"),
        max_length=256
    )
    state = models.CharField(
        _("product state"),
        default="in",
        max_length=2,
        choices=PRODUCT_STATE_CHOICES
    )
    categories = models.ManyToManyField(
        'products.ProductCategory',
        blank=True,
        related_name="products"
    )
    pictures: models.Manager

    @property
    def picture(self) -> 'ProductPicture':
        return self.pictures.first()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")
