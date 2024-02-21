from django.conf import settings
from django.db import models

from users.models import User

# Create your models here.
NULLABLE = {
    'null': True,
    'blank': True,
}


class Breed(models.Model):
    name = models.CharField(max_length=150, verbose_name='порода')
    description = models.TextField(**NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'порода'
        verbose_name_plural = 'породы'


class Dog(models.Model):
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='dogs', verbose_name='порода', null=True)
    nickname = models.CharField(max_length=150, verbose_name='кличка')
    image = models.ImageField(upload_to='app_dogs/', verbose_name='фотография', **NULLABLE)
    birthday = models.DateField(verbose_name='дата рождения', **NULLABLE)
    email = models.EmailField(verbose_name='почта', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)
    is_public = models.BooleanField(default=False)
    price = models.PositiveIntegerField(default=100, verbose_name='цена', **NULLABLE)

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = 'собака'
        verbose_name_plural = 'собаки'
