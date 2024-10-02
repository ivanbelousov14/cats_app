import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from cats_show.models import Breed


@method_decorator(csrf_exempt, name='dispatch')
class BreedView(ListView):
    model = Breed

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        breeds = Breed.objects.all()
        response = []
        for breed in self.object_list:
            response.append({
                'id': breed.pk,
                'name': breed.name,
                'description': breed.description
            })
        return JsonResponse(response, safe=False)


class BreedDetailView(DetailView):
    model = Breed

    def get(self, request, *args, **kwargs):
        breed = self.get_object()

        return JsonResponse({
            'name': breed.name,
            'description': breed.description
        })


@method_decorator(csrf_exempt, name='dispatch')
class BreedCreateView(CreateView):
    model = Breed
    fields = ['name', 'description']

    def post(self, request, *args, **kwargs):
        breed_data = json.loads(request.body)
        breed = Breed.objects.create(
            name=breed_data['name'],
            description=breed_data['description']
        )
        return JsonResponse({
            'name': breed.name,
            'description': breed.description
        })


@method_decorator(csrf_exempt, name='dispatch')
class BreedUpdateView(UpdateView):
    model = Breed
    fields = ['name', 'description']

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        breed_data = json.loads(request.body)
        self.object.name = breed_data['name']
        self.object.description = breed_data['description']

        self.object.save()

        return JsonResponse({
            'name': self.object.name,
            'description': self.object.description
        })

@method_decorator(csrf_exempt, name='dispatch')
class BreedDeleteView(DeleteView):
    model = Breed
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({'status': 'ok'}, status=204)


