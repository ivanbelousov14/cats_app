from django.db import models
from authentication.models import User

MALE = 'm'
FEMALE = 'f'
SEX = [(MALE, 'male'), (FEMALE, 'female')]


class Breed(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'

    def __str__(self):
        return self.name


class Cat(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(null=False)
    gender = models.CharField(max_length=1, choices=SEX, default=MALE, blank=True)
    photo = models.ImageField(upload_to='photo/', default=None)
    description = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Котик'
        verbose_name_plural = 'Котики'

    def __str__(self):
        return self.name




