from django.urls import path
from cats_show.views import BreedListView, BreedDetailView, BreedCreateView, BreedUpdateView, BreedDeleteView
from cats import settings
from django.conf.urls.static import static
urlpatterns = [
    path('breed/', BreedListView.as_view(), name='breed'),
    path('breed/create/', BreedCreateView.as_view()),
    path('breed/<int:pk>/', BreedDetailView.as_view(), name='detail_breed'),
    path('breed/<int:pk>/update/', BreedUpdateView.as_view()),
    path('breed/<int:pk>/delete/', BreedDeleteView.as_view()),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)