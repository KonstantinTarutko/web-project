from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    gender = models.CharField(max_length=2, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)


