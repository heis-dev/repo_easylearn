from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_platform_admin = models.BooleanField(default=False)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = []
