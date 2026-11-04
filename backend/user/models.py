from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, username: str, password: str, **extra_fields) -> CustomUser:
        """Responsável pela criação do usuário no sistema"""

        if not username:
            raise ValueError("O nome de usuário é um campo obriga")

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username: str, password: str, **extra_fields) -> CustomUser:
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)


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

    # se o usuário possuir is_staff ativo, ele pode acessar o django admin, mas não com as permissões totais
    is_staff = models.BooleanField(default=False)

    # se o usupario possuir is_superuser ativo, ele pode acessar o django admin e vai ter todas as permissões
    is_superuser = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.username
