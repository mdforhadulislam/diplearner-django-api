from django.urls import path, include
from api.views import getApiUrls
from .views import *

urlpatterns = [
    path('', getApiUrls),
]
