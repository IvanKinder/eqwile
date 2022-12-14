from django.contrib.auth.models import User
from django.db import models


class Wallet(models.Model):
    """User Wallet model"""

    author = models.OneToOneField(User, verbose_name='author', on_delete=models.CASCADE, blank=False,
                                  null=False)
    cash = models.FloatField(verbose_name='user summary money', null=False, blank=False, default=0)


class AuthorTizerCost(models.Model):
    """One User Tizer cost model"""

    author = models.OneToOneField(User, verbose_name='author', on_delete=models.CASCADE, blank=False,
                                  null=False)
    cost = models.FloatField(verbose_name='one tizer cost', blank=False, null=False, default=50)
