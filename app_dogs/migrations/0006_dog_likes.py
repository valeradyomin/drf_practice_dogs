# Generated by Django 4.2.7 on 2024-02-29 22:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_dogs', '0005_dog_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_likes', to=settings.AUTH_USER_MODEL, verbose_name='лайки'),
        ),
    ]