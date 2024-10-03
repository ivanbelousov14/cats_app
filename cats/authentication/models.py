from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    MALE = 'm'
    FEMALE = 'f'
    SEX = [(MALE, 'male'), (FEMALE, 'female')]

    sex = models.CharField(max_length=1, choices=SEX, default=MALE)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'