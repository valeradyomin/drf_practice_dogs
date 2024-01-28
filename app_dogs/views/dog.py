from rest_framework.generics import RetrieveAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, CreateAPIView

from app_dogs.models import Dog
from app_dogs.serializers.dog import DogSerializer, DogListSerializer, DogDetailSerializer


class DogCreateView(CreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer


class DogDetailView(RetrieveAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogDetailSerializer


class DogDeleteView(DestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer


# class DogListView(ListAPIView):
#     queryset = Dog.objects.all()
#     serializer_class = DogSerializer


class DogListView(ListAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogListSerializer


class DogUpdateView(UpdateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    