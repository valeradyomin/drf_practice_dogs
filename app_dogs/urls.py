from django.urls import path
from rest_framework import routers

from app_dogs.views.breed import BreedViewSet
from app_dogs.views.dog import DogListView, DogCreateView, DogDetailView, DogUpdateView, DogDeleteView

router = routers.DefaultRouter()
router.register(r'breed', BreedViewSet, basename='breeds')

urlpatterns = [
    path('', DogListView.as_view(), name='dog_list'),
    path('create/', DogCreateView.as_view(), name='dog_create'),
    path('detail/<int:pk>/', DogDetailView.as_view(), name='dog_detail'),
    path('update/<int:pk>/', DogUpdateView.as_view(), name='dog_update'),
    path('delete/<int:pk>/', DogDeleteView.as_view(), name='dog_delete'),
] + router.urls
