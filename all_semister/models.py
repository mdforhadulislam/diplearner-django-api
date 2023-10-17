from django.db import models
from book.models import Probidhan
# Create your models here.

class Semister(models.Model):
    semister_number = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.semister_number



class DepartmantName(models.Model):
    departmant_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.departmant_name


