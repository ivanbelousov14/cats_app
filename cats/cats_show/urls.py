from cats_show.views import BreedViewSet, CatViewSet
from django.urls import path
from cats import settings
from django.conf.urls.static import static
from rest_framework import routers

router = routers.SimpleRouter()
router.register('breed', BreedViewSet)
router.register('cat', CatViewSet)

urlpatterns = [
    # path('cat/', CatCreateView.as_view())
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
