from cats_show.views import BreedViewSet
from cats import settings
from django.conf.urls.static import static
from rest_framework import routers

router = routers.SimpleRouter()
router.register('breed', BreedViewSet)

urlpatterns = []

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)