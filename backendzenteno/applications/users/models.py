from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.urls import reverse

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .managers import UserManager

import uuid

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
	user_uuid = models.UUIDField(default=uuid.uuid4, editable=False) 

	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)

	# Manager
	objects = UserManager()

	# Standard methods
	def __str__(self):
		return self.user_name + self.user_email

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)