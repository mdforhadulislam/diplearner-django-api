from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication
from .serializers import RegisterSerializer
from rest_framework import status
from knox.models import AuthToken


def serialize_user(user):
    return {
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name
    }


@api_view(['GET'])
def getApiUrls(request):
    print(request)
    # token = AuthToken.objects.filter(user=1)
    # print(token)
    allUrls = {
        'register': 'http://127.0.0.1:8000/api/register/',
        'login': 'http://127.0.0.1:8000/api/login/',
        'logout': 'http://127.0.0.1:8000/api/logout/'
    }
    return Response(allUrls, status.HTTP_200_OK)


# this is login api only post username and password
@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)
    return Response({
        'user_data': serialize_user(user),
        'token': token
    })


# when create new user post username password email first_name and last_name
@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        return Response({
            "user_info": serialize_user(user),
            "token": token
        })
