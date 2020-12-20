from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.urls import reverse

from .managers import UserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
	# Constants
	USER_ROLE_CHOICE = (
      	(1, 'Empleado'),
      	(2, 'Manager de almuerzos'),
    )
	USERNAME_FIELD = 'user_email'

    # Fields
	user_name = models.CharField(max_length=50)
	user_email = models.EmailField(unique=True, max_length=50)
	user_role = models.PositiveSmallIntegerField(choices=USER_ROLE_CHOICE)

	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)

	# Manager
	objects = UserManager()

	# Standard methods
	def __str__(self):
		return self.user_name + self.user_email