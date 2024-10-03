from rest_framework import serializers
from cats_show.models import Breed, Cat


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class CatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cat
        fields = '__all__'
