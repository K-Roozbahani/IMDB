from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def _create_user_(self, email, first_name, last_name, password=None,
                      is_active=True, is_staff=False, *args, **kwargs):
        # if last_name == None or first_name == None:
        #     raise ValueError('please Enter first name and last name')
        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name,
                          is_active=is_active, is_staff=is_staff)
        if password:
            user.set_password(password)
            user.save()
            return user


    def create_user(self, email, first_name, last_name, password=None, *args, **kwargs):
        return self._create_user_(email, first_name, last_name, password, True, False, *args, **kwargs)

    def create_superuser(self, email, first_name, last_name, password=None, *args, **kwargs):
        return = self._create_user_(email, first_name, last_name, password, True, True, *args, **kwargs)


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=64, blank=True, null=True)
    last_name = models.CharField(max_length=64, blank=True, null=True)
    date_join = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to="users/")
    objects = UserManager

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
