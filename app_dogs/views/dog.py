from rest_framework.generics import RetrieveAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, CreateAPIView, \
    get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from app_dogs.models import Dog
from app_dogs.paginators import DogPaginator
from app_dogs.permissions import IsModerator, IsDogOwner, IsDogPublic
from app_dogs.serializers.breed import DogListSerializer
from app_dogs.serializers.dog import DogSerializer, DogDetailSerializer
from app_dogs.tasks import send_message_about_like
from users.models import User


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


class SetLikeToDog(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = get_object_or_404(User, pk=request.data.get('user'))
        dog = get_object_or_404(Dog, pk=request.data.get('dog'))
        if dog.likes.filter(pk=user.pk).exists():
            return Response({'result': f'Пользователь {user} уже добавил ранее like к {dog}'}, status=200)

        send_message_about_like.delay(user.username)
        dog.likes.add(user)
        return Response({'result': f'Пользователь {user} добавил like к {dog}'}, status=200)
