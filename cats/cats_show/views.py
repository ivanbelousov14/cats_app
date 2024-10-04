from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from cats_show.models import Breed, Cat
from cats_show.permissions import IsOwner
from cats_show.serializers import BreedSerializer, CatSerializer
from rest_framework.viewsets import ModelViewSet

class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)



class CatViewSet(ModelViewSet):

    serializer_class = CatSerializer
    queryset = Cat.objects.all()
    permission_classes = (AllowAny,)

    def get_queryset(self, *args, **kwargs):
        request = self.request
        breed = request.GET.get('breed')
        if breed:
            return Cat.objects.filter(breed__name=breed)
        return super().get_queryset(*args, **kwargs)

    def get_permissions(self):
        permissions_classes = (AllowAny,)
        if self.action in ['update', 'partial_update', 'destroy']:
            permissions_classes = [IsOwner]
        return tuple(permission() for permission in permissions_classes)





