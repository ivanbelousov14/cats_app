from django.urls import path, include

from cats_show.views import index

urlpatterns = [
    path('', index)

]
