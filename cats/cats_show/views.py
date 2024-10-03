import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from cats_show.models import Breed, Cat
from cats_show.serializers import BreedListSerializer, BreedDetailSerializer, BreedCreateSerializer, BreedUpdateSerializer, BreedDeleteSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView


@method_decorator(csrf_exempt, name='dispatch')
class BreedListView(ListAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedListSerializer

    # def get(self, request, *args, **kwargs):
    #     super().get(request, *args, **kwargs)
    #     response = BreedListSerializer(self.object_list, many=True).data
    #     return JsonResponse(response, safe=False)


class BreedDetailView(RetrieveAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedDetailSerializer

    # def get(self, request, *args, **kwargs):
    #     breed = self.get_object()
    #
    #     return JsonResponse(BreedDetailSerializer(breed).data)


# @method_decorator(csrf_exempt, name='dispatch')
class BreedCreateView(CreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedCreateSerializer

    # model = Breed
    # fields = ['name', 'description']
    #
    # def post(self, request, *args, **kwargs):
    #     breed_data = BreedCreateSerializer(data=json.loads(request.body))
    #     if breed_data.is_valid():
    #         breed_data.save()
    #     else:
    #         return JsonResponse(breed_data.errors)
    #     return JsonResponse(breed_data.data)


class BreedUpdateView(UpdateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedUpdateSerializer

    # def post(self, request, *args, **kwargs):
    #     super().post(request, *args, **kwargs)
    #
    #     breed_data = json.loads(request.body)
    #     self.object.name = breed_data['name']
    #     self.object.description = breed_data['description']
    #
    #     self.object.save()
    #
    #     return JsonResponse({
    #         'name': self.object.name,
    #         'description': self.object.description
    #     })


# @method_decorator(csrf_exempt, name='dispatch')
class BreedDeleteView(DestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedDeleteSerializer
    # model = Breed
    # success_url = '/'
    #
    # def delete(self, request, *args, **kwargs):
    #     super().delete(request, *args, **kwargs)
    #     return JsonResponse({'status': 'ok'}, status=204)
    #

@method_decorator(csrf_exempt, name='dispatch')
class CatView(ListView):
    model = Cat

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        response = []
        for cat in self.object_list:
            response.append(
                {
                    'name': cat.name,
                    'color': cat.color,
                    'age': cat.age,
                    'breed': cat.breed,

                }
            )

