from django.urls import path, include
from . import views
from . api import api

urlpatterns = [
    path("", api.urls),
]