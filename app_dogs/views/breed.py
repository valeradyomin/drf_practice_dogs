from rest_framework.viewsets import ModelViewSet

from app_dogs.models import Breed
from app_dogs.serializers.breed import BreedDetailSerializer, BreedSerializer, BreedListSerializer


class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    default_serializer = BreedSerializer
    serializers = {
        'list': BreedListSerializer,
        'retrieve': BreedDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)
