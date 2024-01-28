from rest_framework import serializers
from rest_framework.fields import SerializerMethodField, IntegerField
from rest_framework.relations import SlugRelatedField

from app_dogs.models import Breed, Dog


class DogListSerializer(serializers.ModelSerializer):
    breed = SlugRelatedField(queryset=Breed.objects.all(), slug_field='name')

    class Meta:
        model = Dog
        fields = ('breed', 'nickname',)

# class BreedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Breed
#         fields = '__all__'


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class BreedListSerializer(serializers.ModelSerializer):
    dog_count = IntegerField()

    class Meta:
        model = Breed
        fields = ('name', 'dog_count',)


class BreedDetailSerializer(serializers.ModelSerializer):
    dog_by_breed = SerializerMethodField()

    def get_dog_by_breed(self, breed):
        # return [dog.nickname for dog in Dog.objects.filter(breed=breed)]
        return DogListSerializer(Dog.objects.filter(breed=breed), many=True).data

    class Meta:
        model = Breed
        fields = '__all__'
