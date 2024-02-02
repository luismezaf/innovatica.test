
from django.db import models


class BaseAbstractModel(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False, verbose_name="ID")

    class Meta:
        abstract = True
