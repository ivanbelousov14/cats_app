from rest_framework.permissions import IsAuthenticated
from cats_show.models import Breed, Cat
from cats_show.serializers import BreedSerializer, CatSerializer
from rest_framework.viewsets import ModelViewSet


class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class CatViewSet(ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = [IsAuthenticated]


