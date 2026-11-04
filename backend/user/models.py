from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Modelo usuário personalizado"""

    

    full_name = models.CharField(
        max_length=150,
        blank=False,
        null=False
    )

    username = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        unique=True
    )



