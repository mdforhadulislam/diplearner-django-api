from django.urls import path, include
from .views import *
from knox import views as knox_views

urlpatterns = [
    path('', getApiUrls),
    path('login/', login),
    path('register/', register),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path('books/',include('book.urls'))
]

