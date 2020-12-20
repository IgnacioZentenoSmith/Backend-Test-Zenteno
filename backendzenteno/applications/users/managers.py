from django.db import models

from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, user_email, password, is_staff, is_active, **kwargs):
        user = self.model(
            user_email=user_email,
            is_staff=is_staff,
            is_active=is_active,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self, user_email, password=None, **kwargs):
        return self._create_user(user_email, password, False, True, **kwargs)
