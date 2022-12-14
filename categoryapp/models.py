from django.db import models


class Category(models.Model):
    """Category model"""

    category_name = models.CharField(max_length=64, verbose_name='category name', unique=True, blank=False, null=False)
