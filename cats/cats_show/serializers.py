from rest_framework import serializers
from cats_show.models import Breed


class BreedListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class BreedDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'
            

class BreedCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class BreedUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class BreedDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class CatSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    color = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    photo = serializers.ImageField()
    description = serializers.CharField(max_length=1000)
    user = serializers.IntegerField()
    breed_name = serializers.CharField(max_length=100)

    # class Cat(models.Model):
    #     name = models.CharField(max_length=100)
    #     color = models.CharField(max_length=100)
    #     age = models.IntegerField(null=False)
    #     photo = models.ImageField(upload_to='photo/', null=True)
    #     description = models.TextField(max_length=1000)
    #     user = models.ForeignKey(User, on_delete=models.CASCADE)
    #     breed = models.ForeignKey(Breed, on_delete=models.CASCADE)


