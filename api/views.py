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
def region(request):
    try:
        all_region = Region.objects.all()
        all_region_data_serializer = RegionSerializer(all_region, many=True)
        all_region_data = all_region_data_serializer.data
        return respons_setup('get all region', all_region_data, 200)
    except Exception as error:
        return respons_setup('there was an servier said error', {}, 400)


@api_view(['GET'])
def city(request):
    try:
        all_city = City.objects.all()
        all_city_data_serializer = CitySerializer(all_city, many=True)
        all_city_data = all_city_data_serializer.data
        return respons_setup('get all city', all_city_data, 200)
    except Exception as error:
        return respons_setup('there was an servier said error', {}, 400)


@api_view(['GET'])
def area(request):
    try:
        all_area = Area.objects.all()
        all_area_data_serializer = AreaSerializer(all_area, many=True)
        all_area_data = all_area_data_serializer.data
        return respons_setup('get all area', all_area_data, 200)
    except Exception as error:
        return respons_setup('there was an servier said error', {}, 400)


@api_view(['GET'])
def address(request):
    try:
        all_address = Address.objects.all()
        all_address_data_serializer = AddressSerializer(all_address, many=True)
        all_address_data = all_address_data_serializer.data
        return respons_setup('get all address', all_address_data, 200)
    except Exception as error:
        return respons_setup('there was an servier said error', {}, 400)


@api_view(['GET'])
def user_info(request, id):
    try:
        all_user_info = UserProfileInfo.objects.get(id=id)
        user_info_data_serializer = UserProfileInfoSerializer(all_user_info)
        user_data = user_info_data_serializer.data
        return respons_setup('register succes', user_data, 200)
    except Exception as error:
        return respons_setup('there was an servier said error', {}, 400)
