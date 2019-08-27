"""Attendee Models"""
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Attendee(models.Model):
    """Attendee Model"""

    class Meta:
        db_table = "attendee"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    deviceid = models.CharField(max_length=30)
    isworking = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {} - {}".format(self.timestamp, self.user, self.deviceid)

class Overtime(models.Model):
    """Overtime Model"""

    class Meta:
        db_table = "overtime"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.DateTimeField
    end = models.DateTimeField
    #timestamp = models.DateTimeField
    #isworking = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {} - {}".format(self.user, self.start, self.end)

class AnnualLeave(models.Model):
    """AnnualLeave Model"""

    class Meta:
        db_table = "annualleave"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.DateField
    end = models.DateField

    def __str__(self):
        return "{} - {} - {}".format(self.user, self.start, self.end)

