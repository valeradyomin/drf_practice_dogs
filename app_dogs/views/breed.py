from rest_framework.viewsets import ModelViewSet

from app_dogs.models import Breed
from app_dogs.serializers.breed import BreedSerializer


class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
