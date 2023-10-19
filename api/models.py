from django.db import models
from django.contrib.auth.models import User
from book.models import AllBook
from general_library.models import LibraryBook


BLOOD_GROUP = (
    ("A+", "A+"),
    ("B+", "B+"),
    ("O+", "O+"),
    ("AB+", "AB+"),
    ("A-", "A-"),
    ("B-", "B-"),
    ("O-", "O-"),
    ("AB-", "AB-"),
)


class Region(models.Model):
    region_name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.region_name


class City(models.Model):
    city_name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.city_name


class Area(models.Model):
    area_name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.area_name


class Address(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)


class UserProfileInfo(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_profile_image = models.ImageField(
        upload_to='profile/', blank=True, null=True)
    mobile_number = models.CharField(max_length=12, blank=True, null=True)
    blood_group = models.CharField(
        max_length=20, choices=BLOOD_GROUP, default=' ', blank=True, null=True)
    institute_name = models.CharField(max_length=200, blank=True, null=True)
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, blank=True, null=True)
    area_address = models.TextField(max_length=500, blank=True, null=True)
    bying_book = models.ManyToManyField(AllBook, blank=True, )
    bying_genaral_book = models.ManyToManyField(LibraryBook, blank=True,)
