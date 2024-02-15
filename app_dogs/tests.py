import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app_dogs.models import Dog, Breed


class DogTestCase(APITestCase):

    def setUp(self):
        self.breed = Breed.objects.create(name='Такса', description='Крутая порода')
        self.dog = Dog.objects.create(breed=self.breed, nickname='Такс')

    def test_get_list(self):
        """
        Тестирование функции get_list путем отправки GET-запроса и проверки статуса ответа.
        """
        response = self.client.get(reverse('dog_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.json())

        self.assertEqual(len(response.data), 4)

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "breed": "Такса",
                        "nickname": "Такс"
                    }
                ]
            }
        )

    def test_dog_create(self):
        """
        Тестирование функции create путем отправки POST-запроса с данными собаки и проверки статуса ответа.
        """
        data = {
            "id": self.dog.id,
            "nickname": 'Такс2',
            "is_public": False,
            "breed": self.breed.id,
        }

        response = self.client.post('/dog/create/', data=data)
        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Dog.objects.count(), 2)

    def test_dog_create_nickname_scam_words(self):
        """
        Тест создания прозвища для собаки с обманными словами, используя имитацию запроса и проверяя ожидаемый
        HTTP-код состояния.
        """
        data = {
            "id": self.dog.id,
            "nickname": 'крипта',
            "is_public": False,
            "breed": self.breed.id,
        }

        response = self.client.post('/dog/create/', data=data)
        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {'nickname': ['Текст содержит запрещенные слова']})
