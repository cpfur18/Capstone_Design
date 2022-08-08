from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=100, verbose_name='닉네임')