from rest_framework.generics import RetrieveAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from app_dogs.models import Dog
from app_dogs.paginators import DogPaginator
from app_dogs.permissions import IsModerator, IsDogOwner, IsDogPublic
from app_dogs.serializers.breed import DogListSerializer
from app_dogs.serializers.dog import DogSerializer, DogDetailSerializer


class DogCreateView(CreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    # permission_classes = [IsAuthenticated]
    # For testing
    permission_classes = [AllowAny]


class DogDetailView(RetrieveAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogDetailSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsDogOwner | IsDogPublic]
    # permission_classes = [AllowAny]


class DogDeleteView(DestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    permission_classes = [IsAuthenticated, IsDogOwner]


# class DogListView(ListAPIView):
#     queryset = Dog.objects.all()
#     serializer_class = DogSerializer


class DogListView(ListAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogListSerializer
    # permission_classes = [IsAuthenticated]
    # For testing
    permission_classes = [AllowAny]
    pagination_class = DogPaginator


class DogUpdateView(UpdateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsDogOwner]
