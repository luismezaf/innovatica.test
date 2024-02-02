
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.abstracts.abstract_model import BaseAbstractModel


class ProductCategory(BaseAbstractModel):
    name = models.CharField(
        _("product category name"),
        max_length=256
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("product category")
        verbose_name_plural = _("product categories")
