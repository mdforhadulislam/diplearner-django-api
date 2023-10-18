from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication
from rest_framework import status
from knox.models import AuthToken
from .models import *
from .serializers import *
from utils.app import *


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
        'register': '/api/register/',
        'login': '/api/login/',
        'logout': '/api/logout/'
    }
    return respons_setup('all api urls', allUrls, 200)


# this is login api only post username and password
@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)
    return respons_setup('login success', token, 200)


# when create new user post username password email first_name and last_name
@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        user_data = {
            "user_info": serialize_user(user),
            "token": token,
            'status': 200
        }
        return respons_setup('register succes', user_data, 200)


@api_view(['GET'])
def user_info(request, id):
    # try:
    all_user_info = UserProfileInfo.objects.get(id=id)
    user_info_data_serializer = UserProfileInfoSerializer(all_user_info)
    user_data = user_info_data_serializer.data
    return respons_setup('register succes', user_data, 200)
    # except Exception as error:
    #     print(error)
    #     return respons_setup('there was an servier said error', {}, 400)
