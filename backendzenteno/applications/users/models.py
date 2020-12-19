from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    USER_ROLE_CHOICE = (
      (1, 'employee'),
      (2, 'lunch manager'),
    )

    #PK = id
    """ Modelo de los usuarios del sistema """
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(unique=True, max_length=50)
    user_role = models.PositiveSmallIntegerField(choices=USER_ROLE_CHOICE)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_email'