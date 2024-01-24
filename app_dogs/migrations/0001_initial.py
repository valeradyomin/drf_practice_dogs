# Generated by Django 4.2.7 on 2024-01-24 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='порода')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'порода',
                'verbose_name_plural': 'породы',
            },
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=150, verbose_name='кличка')),
                ('image', models.ImageField(blank=True, null=True, upload_to='app_dogs/', verbose_name='фотография')),
                ('birthday', models.DateField(verbose_name='дата рождения')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='почта')),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app_dogs', to='app_dogs.breed', verbose_name='порода')),
            ],
            options={
                'verbose_name': 'собака',
                'verbose_name_plural': 'собаки',
            },
        ),
    ]