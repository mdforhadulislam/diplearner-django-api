from django.contrib.auth.models import User
from rest_framework import serializers, validators
from .models import *
from book.serializers import AllBookSerializer
from general_library.serializers import LibraryBookSerializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "email", "first_name", "last_name")
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        User.objects.all(), f"A user with that Email already exists."
                    )
                ],
            },
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"]
        )
        return user


class RegionSerializer(serializers.ModelSerializer):
    region_name = serializers.CharField(max_length=200)

    class Meta:
        model = Region
        fields = ('id', 'region_name')


class CitySerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(max_length=200)

    class Meta:
        model = City
        fields = ('id', 'city_name')


class AreaSerializer(serializers.ModelSerializer):
    area_name = serializers.CharField(max_length=200)

    class Meta:
        model = Area
        fields = ('id', 'area_name')


class AddressSerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)
    city = CitySerializer(read_only=True)
    area = AreaSerializer(read_only=True)

    class Meta:
        model = Address
        fields = ('__all__')


class UserProfileInfoSerializer(serializers.ModelSerializer):
    user_id = RegisterSerializer(read_only=True)
    user_profile_image = serializers.ImageField()
    mobile_number = serializers.CharField(max_length=12)
    blood_group = serializers.CharField(max_length=20)
    institute_name = serializers.CharField(max_length=200)
    address = AddressSerializer(read_only=True)
    area_address = serializers.CharField(max_length=500)
    bying_book = AllBookSerializer(many=True)
    bying_genaral_book = LibraryBookSerializer(many=True)

    class Meta:
        model = Area
        fields = ('id', 'user_id', 'user_profile_image', 'mobile_number', 'institute_name',
                  'blood_group', 'address', 'area_address', 'bying_book', 'bying_genaral_book')
