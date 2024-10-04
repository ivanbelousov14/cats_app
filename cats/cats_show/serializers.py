from rest_framework import serializers
from cats_show.models import Breed, Cat
from authentication.models import User


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class CatSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        required=True
    )

    breed = serializers.SlugRelatedField(
        queryset=Breed.objects.all(),
        slug_field='name',
        required=False
    )

    class Meta:
        model = Cat
        fields = '__all__'
