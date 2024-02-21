import requests
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
    price_in_eur = serializers.SerializerMethodField()
    price_in_usd = serializers.SerializerMethodField()

    def get_dog_with_same_breed(self, dog):
        return Dog.objects.filter(breed=dog.breed).count()

    def get_price_in_eur(self, dog):
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=EUR&from=RUB&amount={dog.price}"

        payload = {}
        headers = {
            "apikey": "UrsvIXz1QYo9FYZxeQZ5eUtwUxs2pT6Q"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        result = response.json()

        return result.get('result')

    def get_price_in_usd(self, dog):
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=USD&from=RUB&amount={dog.price}"

        payload = {}
        headers = {
            "apikey": "UrsvIXz1QYo9FYZxeQZ5eUtwUxs2pT6Q"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        result = response.json()

        return result.get('result')

    class Meta:
        model = Dog
        fields = ('breed', 'nickname', 'dog_with_same_breed', 'price_in_eur', 'price_in_usd',)
