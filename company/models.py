"""Company Model"""
from django.db import models

# Create your models here.

class Company(models.Model):
    """Company Model"""
    class Meta:
        db_table = "company"

    code = models.CharField(max_length=10, blank=False, unique=True)
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return "{} - {}".format(self.code, self.name)


class Location(models.Model):
    """Location Model"""
    class Meta:
        db_table = "location"

    name = models.CharField(max_length=30)
    deviceid = models.CharField(max_length=30, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.deviceid, self.name)
