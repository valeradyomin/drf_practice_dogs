from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField

from app_dogs.models import Dog, Breed
from app_dogs.serializers.breed import BreedDetailSerializer


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'


class DogListSerializer(serializers.ModelSerializer):
    breed = SlugRelatedField(queryset=Breed.objects.all(), slug_field='name')

    class Meta:
        model = Dog
        fields = ('breed', 'nickname',)


class DogDetailSerializer(serializers.ModelSerializer):
    breed = BreedDetailSerializer()
    dog_with_same_breed = SerializerMethodField()

    def get_dog_with_same_breed(self, dog):
        return Dog.objects.filter(breed=dog.breed).count()

    class Meta:
        model = Dog
        fields = ('breed', 'nickname', 'dog_with_same_breed',)
