from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    is_active = models.BooleanField(default=False)
    otp_secret_key = models.CharField(max_length=16, blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='custom_user_groups'
    )
    # Add related_name for user_permissions field
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='custom_user_permissions'
    )
