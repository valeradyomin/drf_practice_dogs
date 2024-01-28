from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from app_dogs.models import Breed, Dog


# class BreedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Breed
#         fields = '__all__'

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class BreedListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ('name',)


class BreedDetailSerializer(serializers.ModelSerializer):
    dog_by_breed = SerializerMethodField()

    def get_dog_by_breed(self, breed):
        return [dog.nickname for dog in Dog.objects.filter(breed=breed)]

    class Meta:
        model = Breed
        fields = '__all__'
