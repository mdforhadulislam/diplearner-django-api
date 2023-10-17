from django.urls import path, include
from .views import *
from knox import views as knox_views

urlpatterns = [
    path('', getApiUrls),
    path('auth/login/', login),
    path('auth/register/', register),
    path('auth/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('auth/logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    # path('accounts/<str:id>/',get_accounts),
    
]

