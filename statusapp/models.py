from django.db import models


class Status(models.Model):
    """Status model"""

    STATUS_CHOICES = (
        ('paid', 'Paid'),
        ('rejected', 'Rejected'),
    )

    status_name = models.CharField(max_length=64, choices=STATUS_CHOICES, verbose_name='status name', unique=True,
                                   blank=False, null=False)
