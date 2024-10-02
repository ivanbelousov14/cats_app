from django.urls import path, include
from cats_show.views import BreedView, BreedDetailView, BreedCreateView, BreedUpdateView, BreedDeleteView

urlpatterns = [
    path('breed/', BreedView.as_view(), name='breed'),
    path('breed/create/', BreedCreateView.as_view()),
    path('breed/<int:pk>/', BreedDetailView.as_view(), name='detail_breed'),
    path('breed/<int:pk>/update/', BreedUpdateView.as_view()),
    path('breed/<int:pk>/delete/', BreedDeleteView.as_view()),


]
