from rest_framework import serializers
from rest_framework.fields import SerializerMethodField, IntegerField
from rest_framework.relations import SlugRelatedField

from app_dogs.models import Dog, Breed
from app_dogs.serializers.breed import BreedDetailSerializer
from app_dogs.validators import validator_scam_words


class DogSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(validators=[validator_scam_words])

    class Meta:
        model = Dog
        fields = '__all__'


class DogDetailSerializer(serializers.ModelSerializer):
    breed = BreedDetailSerializer()
    dog_with_same_breed = SerializerMethodField()

    def get_dog_with_same_breed(self, dog):
        return Dog.objects.filter(breed=dog.breed).count()

    class Meta:
        model = Dog
        fields = ('breed', 'nickname', 'dog_with_same_breed',)
