from django.contrib.auth.models import User
from django.db import models

from categoryapp.models import Category
from statusapp.models import Status


class Tizer(models.Model):
    """Tizer model"""

    title = models.CharField(max_length=64, verbose_name='tizer title', blank=False, null=False)
    description = models.TextField(verbose_name='tizer description', blank=False, null=False)
    category = models.ForeignKey(Category, verbose_name='tizer category', on_delete=models.CASCADE, blank=False,
                                 null=False)
    author = models.ForeignKey(User, verbose_name='tizer author', on_delete=models.CASCADE, blank=False, null=False)
    status = models.ForeignKey(Status, verbose_name='tizer status', on_delete=models.CASCADE, default=None, blank=True,
                               null=True)
