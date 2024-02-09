from django.contrib import admin

from app_dogs.models import Breed, Dog


# Register your models here.


@admin.register(Breed)
class AdminBreed(admin.ModelAdmin):
    list_display = ('name', 'description',)
    # verbose_name = 'Порода'


@admin.register(Dog)
class AdminDog(admin.ModelAdmin):
    list_display = ('nickname', 'birthday', 'breed', 'is_public', 'owner',)
    list_filter = ('breed',)
    search_fields = ('nickname',)
    # verbose_name = 'Собаки'