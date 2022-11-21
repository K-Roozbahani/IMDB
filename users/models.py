from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class UserManager(PermissionsMixin):
    pass


class User(AbstractBaseUser):
    email_address = models.EmailField(unique=True)
    first_name = models.CharField(max_length=64, blank=True, null=True)
    last_name = models.CharField(max_length=64, blank=True, null=True)
    date_join = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to="users/")
    objects = UserManager

    USERNAME_FIELD = 'email_address'
    EMAIL_FIELD = 'email_address'
    REQUIRED_FIELDS = ['first_name', 'last_name']
