from rest_framework import serializers

from app_dogs.models import Breed


# class BreedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Breed
#         fields = '__all__'


class BreedListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ('name',)


class BreedDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'
