from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
NULLABLE = {
    'null': True,
    'blank': True,
}


class User(AbstractUser):
    age = models.PositiveIntegerField(**NULLABLE)
