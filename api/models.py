from django.db import models
from django.contrib.auth.models import User


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
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name


class City(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name


class Area(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name


class Address(models.Model):
    address = models.ForeignKey(City, on_delete=models.CASCADE)
    area_address = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.area_address


class UserProfileInfo(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_profile_image = models.ImageField(
        upload_to='profile/', blank=True, null=True)
    mobile_number = models.CharField(max_length=12, blank=True, null=True)
    blood_group = models.CharField(
        max_length=20, choices=BLOOD_GROUP, default=' ')
    institute_name = models.CharField(max_length=200, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

